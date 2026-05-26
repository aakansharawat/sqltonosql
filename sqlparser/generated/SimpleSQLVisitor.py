# Generated from sql_parser/grammar/SimpleSQL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleSQLParser import SimpleSQLParser
else:
    from SimpleSQLParser import SimpleSQLParser

# This class defines a complete generic visitor for a parse tree produced by SimpleSQLParser.

class SimpleSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleSQLParser#sqlStatement.
    def visitSqlStatement(self, ctx:SimpleSQLParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#selectStatement.
    def visitSelectStatement(self, ctx:SimpleSQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#SelectAll.
    def visitSelectAll(self, ctx:SimpleSQLParser.SelectAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#SelectColumns.
    def visitSelectColumns(self, ctx:SimpleSQLParser.SelectColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#columnName.
    def visitColumnName(self, ctx:SimpleSQLParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#tableName.
    def visitTableName(self, ctx:SimpleSQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#joinClause.
    def visitJoinClause(self, ctx:SimpleSQLParser.JoinClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#whereClause.
    def visitWhereClause(self, ctx:SimpleSQLParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#orderByClause.
    def visitOrderByClause(self, ctx:SimpleSQLParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#orderByItem.
    def visitOrderByItem(self, ctx:SimpleSQLParser.OrderByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#SimpleCondition.
    def visitSimpleCondition(self, ctx:SimpleSQLParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#JoinCondition.
    def visitJoinCondition(self, ctx:SimpleSQLParser.JoinConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#operator.
    def visitOperator(self, ctx:SimpleSQLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#value.
    def visitValue(self, ctx:SimpleSQLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSQLParser#limitClause.
    def visitLimitClause(self, ctx:SimpleSQLParser.LimitClauseContext):
        return self.visitChildren(ctx)



del SimpleSQLParser