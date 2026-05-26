"""
sql_to_dynamodb.py
==================
Generate boto3 DynamoDB Python code from a Unified AST (UAST).

Uses scan() when filters are present (demo-friendly). For production,
partition-key queries should be configured separately.
"""

from transformer.uast_helpers import validate_select_uast


def _python_literal(value):
    """Format a UAST value as a Python literal for boto3 Attr calls."""
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).strip()
    if text.startswith("'") and text.endswith("'"):
        return repr(text[1:-1])
    if text.isdigit():
        return text
    return repr(text)

# Mongo operator in UAST -> boto3 Attr method name
MONGO_TO_ATTR = {
    "$eq": "eq",
    "$gt": "gt",
    "$lt": "lt",
    "$gte": "gte",
    "$lte": "lte",
    "$ne": "ne",
}


class DynamoDBQueryGenerator:
    """Build boto3 table.scan() / query-style snippets from UAST."""

    def generate(self, uast):
        validate_select_uast(uast)

        table = uast["collection"]
        filter_dict = uast.get("filter") or {}
        limit = uast.get("limit")

        lines = [
            "import boto3",
            "from boto3.dynamodb.conditions import Attr",
            "",
            f"dynamodb = boto3.resource('dynamodb')",
            f"table = dynamodb.Table('{table}')",
            "",
        ]

        if filter_dict:
            expr = self._build_filter_expression(filter_dict)
            call = f"response = table.scan(\n    FilterExpression={expr}"
        else:
            call = "response = table.scan("

        if limit is not None:
            if filter_dict:
                lines.append(call + f",\n    Limit={limit}\n)")
            else:
                lines.append(call + f"\n    Limit={limit}\n)")
        else:
            if filter_dict:
                lines.append(call + "\n)")
            else:
                lines.append(call + ")")

        lines.append("items = response.get('Items', [])")
        return "\n".join(lines)

    def _build_filter_expression(self, filter_dict):
        """Turn UAST filter into chained Attr() calls."""
        parts = []
        for column, condition in filter_dict.items():
            if isinstance(condition, dict):
                for mongo_op, val in condition.items():
                    method = MONGO_TO_ATTR.get(mongo_op, "eq")
                    parts.append(f"Attr('{column}').{method}({_python_literal(val)})")
            else:
                parts.append(f"Attr('{column}').eq({_python_literal(condition)})")

        if len(parts) == 1:
            return parts[0]
        # Chain with & for multiple conditions
        result = parts[0]
        for part in parts[1:]:
            result = f"({result}) & ({part})"
        return result


def generate_dynamodb(uast):
    """Public entry point used by web server and CLI."""
    return DynamoDBQueryGenerator().generate(uast)


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
    print(generate_dynamodb(sample))
