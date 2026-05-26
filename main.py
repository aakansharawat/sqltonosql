"""
main.py
=======
CLI entry point for the SQL to NoSQL transpiler.

Usage:
  python main.py "SELECT name FROM users WHERE age > 25"
  python main.py "SELECT * FROM products LIMIT 10" --target cassandra
  python main.py --interactive
"""

import argparse
import json
import sys

from ast_to_uast import convert_ast_to_uast
from sql_parser.ast_builder import build_ast
from sql_parser.sql_parser import SQLParser, SQLSyntaxError
from transformer import (
    generate_cassandra,
    generate_dynamodb,
    generate_mongo_query,
    generate_redis,
)

# Target platform -> generator function
GENERATORS = {
    "mongodb": generate_mongo_query,
    "cassandra": generate_cassandra,
    "dynamodb": generate_dynamodb,
    "redis": generate_redis,
}

PLATFORM_LABELS = {
    "mongodb": "MongoDB",
    "cassandra": "Cassandra CQL",
    "dynamodb": "DynamoDB",
    "redis": "Redis",
}


def transpile(sql_query, target="mongodb", show_output=True):
    """
    Full pipeline: SQL -> AST -> UAST -> target query string.

    Returns:
        tuple: (ast_dict, uast_dict, target_query_str)
    """
    target = target.lower()
    if target not in GENERATORS:
        raise ValueError(
            f"Unknown target '{target}'. Choose from: {', '.join(GENERATORS)}"
        )

    label = PLATFORM_LABELS.get(target, target)

    if show_output:
        print("\n" + "=" * 60)
        print(f"SQL to {label} Transpiler")
        print("=" * 60)
        print(f"\nParsing: {sql_query}")

    parser = SQLParser()
    parse_tree = parser.parse(sql_query)
    ast = build_ast(parse_tree)
    uast = convert_ast_to_uast(ast)
    target_query = GENERATORS[target](uast)

    if show_output:
        print("\nAST:")
        print("-" * 60)
        print(json.dumps(ast, indent=2))
        print("\nUAST:")
        print("-" * 60)
        print(json.dumps(uast, indent=2))
        print(f"\n{label} output:")
        print("-" * 60)
        print(target_query)
        print("-" * 60)

    return ast, uast, target_query


def run_interactive():
    """Read SQL queries from stdin until the user quits."""
    print("\n" + "=" * 60)
    print("Interactive mode (quit / exit / q to leave)")
    print(f"Targets: {', '.join(GENERATORS.keys())}")
    print("=" * 60)

    while True:
        try:
            query = input("\nSQL> ").strip()
            if query.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            if not query:
                continue

            target = input("Target [mongodb]: ").strip() or "mongodb"
            transpile(query, target=target, show_output=True)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="SQL to NoSQL transpiler (MongoDB, Cassandra, DynamoDB, Redis)",
    )
    parser.add_argument("query", nargs="?", help="SQL query to transpile")
    parser.add_argument(
        "-t", "--target",
        default="mongodb",
        choices=list(GENERATORS.keys()),
        help="Output platform (default: mongodb)",
    )
    parser.add_argument("-o", "--output", help="Write AST JSON to this file")
    parser.add_argument("--uast", help="Write UAST JSON to this file")
    parser.add_argument("--out-query", help="Write target query to this file")
    parser.add_argument("-i", "--interactive", action="store_true")
    args = parser.parse_args()

    if args.interactive or not args.query:
        run_interactive()
        return

    try:
        ast, uast, target_query = transpile(args.query, target=args.target)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(ast, f, indent=2)
        if args.uast:
            with open(args.uast, "w", encoding="utf-8") as f:
                json.dump(uast, f, indent=2)
        if args.out_query:
            with open(args.out_query, "w", encoding="utf-8") as f:
                f.write(target_query)

        print("\nDone.")
    except (SQLSyntaxError, ValueError) as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
