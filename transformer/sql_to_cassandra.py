"""
sql_to_cassandra.py
===================
Generate Apache Cassandra CQL from a Unified AST (UAST).

Pipeline: SQL -> AST -> UAST -> CQL string
"""

from transformer.uast_helpers import (
    validate_select_uast,
    filter_to_cql_conditions,
    projection_columns,
    sort_to_order_by,
)


class CassandraQueryGenerator:
    """Build CQL SELECT statements from normalized UAST."""

    def generate(self, uast):
        validate_select_uast(uast)

        table = uast["collection"]
        columns = projection_columns(uast.get("projection"))
        col_clause = ", ".join(columns)

        parts = [f"SELECT {col_clause}", f"FROM {table}"]

        conditions = filter_to_cql_conditions(uast.get("filter"))
        if conditions:
            parts.append("WHERE " + " AND ".join(conditions))

        order_items = sort_to_order_by(uast.get("sort"))
        if order_items:
            order_str = ", ".join(f"{col} {direction}" for col, direction in order_items)
            parts.append(f"ORDER BY {order_str}")

        limit = uast.get("limit")
        if limit is not None:
            parts.append(f"LIMIT {limit}")

        # Non-key filters often need ALLOW FILTERING in Cassandra
        if conditions:
            parts.append("ALLOW FILTERING")

        return " ".join(parts) + ";"


def generate_cassandra(uast):
    """Public entry point used by web server and CLI."""
    return CassandraQueryGenerator().generate(uast)


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
    print(generate_cassandra(sample))
