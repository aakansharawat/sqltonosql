"""
tests/test_pipeline.py
======================
End-to-end tests: SQL -> AST -> UAST -> all target generators.
"""

import sys
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from ast_to_uast import convert_ast_to_uast
from sql_parser.ast_builder import build_ast
from sql_parser.sql_parser import SQLParser
from transformer.sql_to_cassandra import generate_cassandra
from transformer.sql_to_dynamodb import generate_dynamodb
from transformer.sql_to_mongo import generate_mongo_query
from transformer.sql_to_redis import generate_redis

SQL = "SELECT name, age FROM users WHERE age > 25 LIMIT 5"


def _uast():
    tree = SQLParser().parse(SQL)
    ast = build_ast(tree)
    return convert_ast_to_uast(ast)


def test_mongodb():
    out = generate_mongo_query(_uast())
    assert "db.users.find" in out
    assert "limit(5)" in out.lower() or ".limit(5)" in out


def test_cassandra():
    out = generate_cassandra(_uast())
    assert "SELECT" in out
    assert "FROM users" in out
    assert "age >" in out
    assert "LIMIT 5" in out


def test_dynamodb():
    out = generate_dynamodb(_uast())
    assert "boto3" in out
    assert "Table('users')" in out
    assert "Attr('age').gt" in out


def test_redis():
    out = generate_redis(_uast())
    assert "users" in out


if __name__ == "__main__":
    test_mongodb()
    test_cassandra()
    test_dynamodb()
    test_redis()
    print("All pipeline tests passed.")
