"""
ast_builder.py
Converts ANTLR4 parse tree into clean JSON Abstract Syntax Tree (AST)
"""

import sys

try:
    from .generated.SimpleSQLParser import SimpleSQLParser
    from .generated.SimpleSQLVisitor import SimpleSQLVisitor
except ImportError:
    print("ERROR: Parser not generated yet!")
    print("Please run: antlr4 -Dlanguage=Python3 -o parser/generated parser/grammar/SimpleSQL.g4")
    sys.exit(1)


class ASTBuilder(SimpleSQLVisitor):
    """
    Visitor pattern to traverse ANTLR4 parse tree and build AST
    """
    
    def visitSqlStatement(self, ctx):
        """
        Visit the root SQL statement
        Returns the complete AST
        """
        return self.visit(ctx.selectStatement())
    
    def visitSelectStatement(self, ctx):
        """
        Visit SELECT statement and build AST
        
        Structure:
        {
            "type": "SELECT",
            "columns": [...],
            "table": "...",
            "joins": [...],
            "where": {...},
            "orderBy": [...],
            "limit": ...
        }
        """
        ast = {
            "type": "SELECT"
        }
        
        # Get columns
        ast["columns"] = self.visit(ctx.columnList())
        
        # Get table name
        ast["table"] = ctx.tableName().getText()
        
        # Get JOINs (if any)
        if ctx.joinClause():
            ast["joins"] = [self.visit(join) for join in ctx.joinClause()]
        
        # Get WHERE clause (if any)
        if ctx.whereClause():
            ast["where"] = self.visit(ctx.whereClause())
        
        # Get ORDER BY clause (if any)
        if ctx.orderByClause():
            ast["orderBy"] = self.visit(ctx.orderByClause())
        
        # Get LIMIT (if any)
        if ctx.limitClause():
            ast["limit"] = self.visit(ctx.limitClause())
        
        return ast
    
    def visitSelectAll(self, ctx):
        """
        Visit SELECT * (select all columns)
        Returns: ["*"]
        """
        return ["*"]
    
    def visitSelectColumns(self, ctx):
        """
        Visit SELECT column1, column2, ...
        Returns: ["column1", "column2", ...]
        """
        columns = []
        for col in ctx.columnName():
            columns.append(col.getText())
        return columns
    
    def visitJoinClause(self, ctx):
        """
        Visit JOIN clause
        
        Returns:
        {
            "type": "JOIN",
            "table": "...",
            "on": {...}
        }
        """
        return {
            "type": "JOIN",
            "table": ctx.tableName().getText(),
            "on": self.visit(ctx.condition())
        }
    
    def visitWhereClause(self, ctx):
        """
        Visit WHERE clause
        Returns the condition
        """
        return self.visit(ctx.condition())
    
    def visitSimpleCondition(self, ctx):
        """
        Visit simple condition (e.g., age > 25)
        
        Returns:
        {
            "column": "age",
            "operator": ">",
            "value": "25"
        }
        """
        return {
            "column": ctx.columnName().getText(),
            "operator": ctx.operator().getText(),
            "value": self.visit(ctx.value())
        }
    
    def visitJoinCondition(self, ctx):
        """
        Visit join condition (e.g., users.id = orders.user_id)
        
        Returns:
        {
            "left": "users.id",
            "right": "orders.user_id"
        }
        """
        column_names = ctx.columnName()
        return {
            "left": column_names[0].getText(),
            "right": column_names[1].getText()
        }
    
    def visitValue(self, ctx):
        """
        Visit value (number or string)
        Returns the value as string
        """
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            # Remove quotes from string
            return ctx.STRING().getText().strip("'")
        return ""
    
    def visitLimitClause(self, ctx):
        """
        Visit LIMIT clause
        Returns the limit number as integer
        """
        return int(ctx.NUMBER().getText())
    
    def visitOrderByClause(self, ctx):
        """
        Visit ORDER BY clause
        Returns list of order by items
        """
        items = []
        for item in ctx.orderByItem():
            items.append(self.visit(item))
        return items
    
    def visitOrderByItem(self, ctx):
        """
        Visit ORDER BY item
        Returns: {"column": "...", "direction": "ASC"|"DESC"}
        """
        column = ctx.columnName().getText()
        direction = "ASC"  # default
        
        if ctx.DESC():
            direction = "DESC"
        elif ctx.ASC():
            direction = "ASC"
        
        return {
            "column": column,
            "direction": direction
        }


def build_ast(parse_tree):
    """
    Convert ANTLR4 parse tree to AST
    
    Args:
        parse_tree: ANTLR4 parse tree
        
    Returns:
        dict: Abstract Syntax Tree as dictionary
    """
    builder = ASTBuilder()
    ast = builder.visit(parse_tree)
    return ast


# Test the AST builder
if __name__ == "__main__":
    from parser.parser import SQLParser
    import json
    
    print("=" * 60)
    print("AST Builder Test")
    print("=" * 60)
    
    # Test query
    sql = "SELECT users.name, orders.total FROM users JOIN orders ON users.id = orders.user_id WHERE users.age > 18 LIMIT 10;"
    
    print(f"\nSQL: {sql}\n")
    
    # Parse SQL
    parser = SQLParser()
    parse_tree = parser.parse(sql)
    
    # Build AST
    ast = build_ast(parse_tree)
    
    # Print AST as JSON
    print("AST (JSON):")
    print(json.dumps(ast, indent=2))
    
    print("\n" + "=" * 60)
