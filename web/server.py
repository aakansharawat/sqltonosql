#!/usr/bin/env python3
"""
web/server.py
=============
Flask API for the SQL to NoSQL transpiler.

Pipeline per request:
  SQL -> parse (ANTLR) -> AST -> UAST -> target NoSQL query string
"""

import json
import os
import sys
import traceback
from pathlib import Path

# Project root on sys.path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

from ast_to_uast import convert_ast_to_uast
from sql_parser.ast_builder import build_ast
from sql_parser.sql_parser import SQLParser, SQLSyntaxError
from transformer.sql_to_cassandra import generate_cassandra
from transformer.sql_to_dynamodb import generate_dynamodb
from transformer.sql_to_mongo import generate_mongo_query
from transformer.sql_to_redis import generate_redis

app = Flask(__name__, template_folder="templates")
CORS(app)
app.config["SECRET_KEY"] = "sql-to-nosql-transpiler"

# Strategy map: target id -> generator callable
GENERATORS = {
    "mongodb": generate_mongo_query,
    "cassandra": generate_cassandra,
    "dynamodb": generate_dynamodb,
    "redis": generate_redis,
}

PLATFORM_NAMES = {
    "mongodb": "MongoDB",
    "cassandra": "Cassandra CQL",
    "dynamodb": "DynamoDB (boto3)",
    "redis": "Redis Commands",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/styles.css")
def styles():
    return send_from_directory(".", "styles.css", mimetype="text/css")


@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js", mimetype="application/javascript")


@app.route("/convert", methods=["POST"])
def convert():
    """
    POST JSON: { "sql": "...", "target": "mongodb" }
    Returns: { "ast", "uast", "target", "platform" }
    """
    try:
        data = request.get_json() or {}
        sql_query = (data.get("sql") or "").strip()
        target = (data.get("target") or "mongodb").lower()

        if not sql_query:
            return jsonify({"error": "No SQL query provided"}), 400

        if target not in GENERATORS:
            return jsonify({
                "error": f"Unsupported target: {target}",
                "available": list(GENERATORS.keys()),
            }), 400

        parser = SQLParser()
        parse_tree = parser.parse(sql_query)
        ast = build_ast(parse_tree)
        uast = convert_ast_to_uast(ast)
        target_query = GENERATORS[target](uast)

        return jsonify({
            "ast": json.dumps(ast, indent=2),
            "uast": json.dumps(uast, indent=2),
            "target": target_query,
            "platform": PLATFORM_NAMES.get(target, target),
        })

    except SQLSyntaxError as e:
        return jsonify({"error": f"SQL Syntax Error: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Conversion Error: {str(e)}"}), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


@app.route("/platforms", methods=["GET"])
def get_platforms():
    platforms = [
        {"id": key, "name": PLATFORM_NAMES.get(key, key)}
        for key in GENERATORS
    ]
    return jsonify({"platforms": platforms})


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "sql-to-nosql-transpiler",
        "platforms": list(GENERATORS.keys()),
    })


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(_error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    template_dir = Path(__file__).parent / "templates"
    if not template_dir.exists():
        print(f"Templates not found: {template_dir}")
        sys.exit(1)

    port = int(os.getenv("PORT", "5000"))
    print("=" * 60)
    print("SQL to NoSQL Transpiler - Web Server")
    print("=" * 60)
    print(f"Platforms: {', '.join(GENERATORS.keys())}")
    print(f"Open: http://localhost:{port}")
    print("=" * 60)

    try:
        app.run(host="0.0.0.0", port=port, debug=False)
    except KeyboardInterrupt:
        print("\nServer stopped.")
