"""
sql_to_redis.py
===============
Generate Redis command suggestions from a Unified AST (UAST).

Redis has no SQL equivalent for arbitrary WHERE/LIMIT on tabular data.
This generator maps simple SELECT patterns to Redis data-structure commands
and documents limitations when SQL features cannot map 1:1.
"""

from transformer.uast_helpers import (
    validate_select_uast,
    projection_columns,
    filter_to_cql_conditions,
)


class RedisQueryGenerator:
    """Suggest Redis commands and notes for a SQL-like SELECT in UAST form."""

    def generate(self, uast):
        validate_select_uast(uast)

        table = uast["collection"]
        columns = projection_columns(uast.get("projection"))
        filter_dict = uast.get("filter") or {}
        limit = uast.get("limit")
        sort = uast.get("sort")

        lines = [
            f"# Redis mapping for: SELECT ... FROM {table}",
            f"# Key pattern suggestion: {table}:<id>  (hash per row)",
            "",
        ]

        if not filter_dict and not sort and (not limit or limit is None):
            # Simple full read — use hash or key scan
            if columns == ["*"]:
                lines.extend([
                    f"# Fetch all fields for keys matching '{table}:*'",
                    f"KEYS {table}:*",
                    f"HGETALL {table}:<id>   # run per key returned by KEYS/SCAN",
                ])
            else:
                fields = ", ".join(columns)
                lines.extend([
                    f"# Read specific hash fields: {fields}",
                    f"HMGET {table}:<id> {' '.join(columns)}",
                ])
        else:
            # Filtered / sorted / limited — application-level filtering
            conditions = filter_to_cql_conditions(filter_dict)
            lines.append("# SQL filters cannot run inside Redis directly.")
            lines.append("# Use application code or RediSearch for complex queries.")
            lines.append("")
            if conditions:
                lines.append(f"# Equivalent filter intent: {' AND '.join(conditions)}")
            if sort:
                lines.append(f"# Sort: {sort}")
            if limit:
                lines.append(f"# Limit: {limit}")
            lines.extend([
                "",
                f"SCAN 0 MATCH {table}:* COUNT 100",
                "# For each key, HGETALL and filter in your application layer",
            ])

        return "\n".join(lines)


def generate_redis(uast):
    """Public entry point used by web server and CLI."""
    return RedisQueryGenerator().generate(uast)


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

    sample = {
        "operation": "SELECT",
        "collection": "users",
        "projection": ["name", "age"],
        "filter": {"age": {"$gt": 25}},
        "limit": 10,
    }
    print(generate_redis(sample))
