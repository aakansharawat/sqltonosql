"""
uast_helpers.py
===============
Shared helpers for reading Unified AST (UAST) structures produced by ast_to_uast.py.
All NoSQL generators use the same UAST shape for SELECT queries.
"""

# Map Mongo-style operators (used in UAST filters) to human-readable SQL-style ops
MONGO_TO_SQL_OP = {
    "$eq": "=",
    "$gt": ">",
    "$lt": "<",
    "$gte": ">=",
    "$lte": "<=",
    "$ne": "!=",
}


def validate_select_uast(uast):
    """Ensure UAST is a dict with operation SELECT and a collection name."""
    if not isinstance(uast, dict):
        raise ValueError("UAST must be a dictionary")
    if uast.get("operation") != "SELECT":
        raise ValueError(
            f"Unsupported operation: {uast.get('operation')}. Only SELECT is supported."
        )
    if not uast.get("collection"):
        raise ValueError("Collection/table name is required in UAST")


def format_value(value):
    """Format a literal for CQL/SQL-like output (quote strings, leave numbers bare)."""
    if isinstance(value, str):
        # Already quoted in SQL AST
        if value.startswith("'") and value.endswith("'"):
            return value
        return f"'{value}'"
    return str(value)


def filter_to_cql_conditions(filter_dict):
    """
    Convert UAST filter dict to CQL WHERE fragments.
    Example: {"age": {"$gt": 25}} -> ['age > 25']
    """
    if not filter_dict:
        return []

    conditions = []
    for column, condition in filter_dict.items():
        if isinstance(condition, dict):
            for mongo_op, val in condition.items():
                sql_op = MONGO_TO_SQL_OP.get(mongo_op, "=")
                conditions.append(f"{column} {sql_op} {format_value(val)}")
        else:
            # Equality shorthand: {"status": "active"}
            conditions.append(f"{column} = {format_value(condition)}")
    return conditions


def projection_columns(projection):
    """Return column list from UAST projection, or ['*'] for all fields."""
    if not projection or projection == "*":
        return ["*"]
    if isinstance(projection, list):
        return projection
    return [projection]


def sort_to_order_by(sort_dict):
    """Convert UAST sort {col: 1|-1} to [(col, 'ASC'|'DESC'), ...]."""
    if not sort_dict:
        return []
    items = []
    for column, direction in sort_dict.items():
        items.append((column, "DESC" if direction == -1 else "ASC"))
    return items
