"""
ast_to_uast.py
==============
AST to Unified AST (UAST) Converter

This module normalizes SQL Abstract Syntax Tree (AST) into a unified format
that's ready for MongoDB code generation.

Part of: SQL to MongoDB Transpiler
Author: Team Codecrew
"""

import json


class ASTToUASTConverter:
    """
    Converts SQL AST to Unified AST (UAST) format.
    
This normalization layer prepares the AST for all NoSQL generators
by converting SQL-specific structures to a platform-neutral format.
    """
    
    # SQL operator to MongoDB operator mapping
    OPERATOR_MAP = {
        ">": "$gt",      # Greater than
        "<": "$lt",      # Less than
        "=": "$eq",      # Equal
        ">=": "$gte",    # Greater than or equal
        "<=": "$lte",    # Less than or equal
        "!=": "$ne",     # Not equal
        "<>": "$ne"      # Not equal (alternative syntax)
    }
    
    def convert(self, ast_dict):
        """
        Main conversion function: AST → UAST
        
        Args:
            ast_dict (dict): AST from SQL parser
            
        Returns:
            dict: Unified AST ready for MongoDB generation
            
        Raises:
            ValueError: If AST is invalid or query type unsupported
            
        Example:
            >>> converter = ASTToUASTConverter()
            >>> ast = {"type": "SELECT", "table": "users", "columns": ["*"]}
            >>> uast = converter.convert(ast)
            >>> print(uast)
            {"operation": "SELECT", "collection": "users", "projection": "*"}
        """
        # Validate input
        self._validate_ast(ast_dict)
        
        # Initialize UAST
        uast = {
            "operation": "SELECT"
        }
        
        # Extract and convert components
        uast["collection"] = self._extract_collection(ast_dict)
        uast["projection"] = self._extract_projection(ast_dict)
        
        # Optional components (only add if present)
        filter_clause = self._extract_filter(ast_dict)
        if filter_clause is not None:
            uast["filter"] = filter_clause
        
        sort_clause = self._extract_orderby(ast_dict)
        if sort_clause is not None:
            uast["sort"] = sort_clause
        
        limit_value = self._extract_limit(ast_dict)
        if limit_value is not None:
            uast["limit"] = limit_value
        
        return uast
    
    def _validate_ast(self, ast_dict):
        """
        Validate the input AST structure
        
        Args:
            ast_dict: Input to validate
            
        Raises:
            ValueError: If AST is invalid
        """
        if not isinstance(ast_dict, dict):
            raise ValueError("AST must be a dictionary")
        
        query_type = ast_dict.get("type")
        if not query_type:
            raise ValueError("AST must have a 'type' field")
        
        if query_type != "SELECT":
            raise ValueError(
                f"Unsupported query type: '{query_type}'. "
                f"Only SELECT queries are supported in this MVP version."
            )
    
    def _extract_collection(self, ast_dict):
        """
        Extract collection name (MongoDB equivalent of SQL table)
        
        Args:
            ast_dict (dict): AST
            
        Returns:
            str: Collection name
            
        Raises:
            ValueError: If no table specified
        """
        table = ast_dict.get("table")
        
        if not table:
            raise ValueError("No table specified in SELECT query")
        
        return table
    
    def _extract_projection(self, ast_dict):
        """
        Extract projection (columns to select)
        
        MongoDB projection can be:
        - "*" for all fields
        - List of specific field names
        
        Args:
            ast_dict (dict): AST
            
        Returns:
            str or list: "*" for all columns, or list of column names
        """
        columns = ast_dict.get("columns", [])
        
        # No columns specified → default to all
        if not columns:
            return "*"
        
        # Check if SELECT *
        if columns == ["*"] or columns == "*":
            return "*"
        
        # Return list of specific columns
        return columns
    
    def _extract_filter(self, ast_dict):
        """
        Convert SQL WHERE clause to MongoDB filter
        
        SQL: WHERE age > 25
        MongoDB: {"age": {"$gt": 25}}
        
        Args:
            ast_dict (dict): AST
            
        Returns:
            dict or None: MongoDB filter object, or None if no WHERE clause
        """
        where_clause = ast_dict.get("where")
        
        # No WHERE clause
        if not where_clause:
            return None
        
        # Extract WHERE components
        column = where_clause.get("column")
        operator = where_clause.get("operator")
        value = where_clause.get("value")
        
        # Validate components
        if not column or not operator:
            return None
        
        # Convert SQL operator to MongoDB operator
        mongo_operator = self._convert_operator(operator)
        
        # Build MongoDB filter
        if mongo_operator == "$eq":
            # MongoDB allows simple syntax for equality
            # {field: value} instead of {field: {$eq: value}}
            return {column: value}
        else:
            # Other operators need explicit syntax
            return {column: {mongo_operator: value}}
    
    def _convert_operator(self, sql_operator):
        """
        Convert SQL comparison operator to MongoDB operator
        
        Args:
            sql_operator (str): SQL operator (e.g., ">", "<=")
            
        Returns:
            str: MongoDB operator (e.g., "$gt", "$lte")
        """
        # Look up in mapping, default to $eq if not found
        return self.OPERATOR_MAP.get(sql_operator, "$eq")
    
    def _extract_limit(self, ast_dict):
        """
        Extract LIMIT value (pagination)
        
        Args:
            ast_dict (dict): AST
            
        Returns:
            int or None: Limit value as integer, or None if not specified
        """
        limit = ast_dict.get("limit")
        
        if limit is None:
            return None
        
        # Convert to integer (handle both int and string)
        try:
            return int(limit)
        except (ValueError, TypeError):
            # Invalid limit value - ignore it
            return None
    
    def _extract_orderby(self, ast_dict):
        """
        Extract ORDER BY clause and convert to MongoDB sort format
        
        SQL: ORDER BY age DESC, name ASC
        MongoDB: {"age": -1, "name": 1}
        
        Args:
            ast_dict (dict): AST
            
        Returns:
            dict or None: MongoDB sort object, or None if no ORDER BY clause
        """
        orderby = ast_dict.get("orderBy")
        
        if not orderby:
            return None
        
        sort_obj = {}
        
        for item in orderby:
            column = item.get("column")
            direction = item.get("direction", "ASC").upper()
            
            if column:
                # MongoDB: 1 for ascending, -1 for descending
                sort_value = 1 if direction == "ASC" else -1
                sort_obj[column] = sort_value
        
        return sort_obj if sort_obj else None


# Convenience function for simple usage
def convert_ast_to_uast(ast_dict):
    
    converter = ASTToUASTConverter()
    return converter.convert(ast_dict)


# ============================================================================
# MAIN
# ============================================================================
if __name__ == "__main__":
    # Test the converter
    test_ast = {
        "type": "SELECT",
        "columns": ["name", "age"],
        "table": "users",
        "where": {
            "column": "age",
            "operator": ">",
            "value": "25"
        },
        "limit": 10
    }
    result = convert_ast_to_uast(test_ast)
    print(json.dumps(result, indent=2))
