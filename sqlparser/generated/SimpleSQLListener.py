# Generated from sql_parser/grammar/SimpleSQL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleSQLParser import SimpleSQLParser
else:
    from SimpleSQLParser import SimpleSQLParser

# This class defines a complete listener for a parse tree produced by SimpleSQLParser.
class SimpleSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleSQLParser#sqlStatement.
    def enterSqlStatement(self, ctx:SimpleSQLParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#sqlStatement.
    def exitSqlStatement(self, ctx:SimpleSQLParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#selectStatement.
    def enterSelectStatement(self, ctx:SimpleSQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#selectStatement.
    def exitSelectStatement(self, ctx:SimpleSQLParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#SelectAll.
    def enterSelectAll(self, ctx:SimpleSQLParser.SelectAllContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#SelectAll.
    def exitSelectAll(self, ctx:SimpleSQLParser.SelectAllContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#SelectColumns.
    def enterSelectColumns(self, ctx:SimpleSQLParser.SelectColumnsContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#SelectColumns.
    def exitSelectColumns(self, ctx:SimpleSQLParser.SelectColumnsContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#columnName.
    def enterColumnName(self, ctx:SimpleSQLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#columnName.
    def exitColumnName(self, ctx:SimpleSQLParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#tableName.
    def enterTableName(self, ctx:SimpleSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#tableName.
    def exitTableName(self, ctx:SimpleSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#joinClause.
    def enterJoinClause(self, ctx:SimpleSQLParser.JoinClauseContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#joinClause.
    def exitJoinClause(self, ctx:SimpleSQLParser.JoinClauseContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#whereClause.
    def enterWhereClause(self, ctx:SimpleSQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#whereClause.
    def exitWhereClause(self, ctx:SimpleSQLParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#orderByClause.
    def enterOrderByClause(self, ctx:SimpleSQLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#orderByClause.
    def exitOrderByClause(self, ctx:SimpleSQLParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#orderByItem.
    def enterOrderByItem(self, ctx:SimpleSQLParser.OrderByItemContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#orderByItem.
    def exitOrderByItem(self, ctx:SimpleSQLParser.OrderByItemContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#SimpleCondition.
    def enterSimpleCondition(self, ctx:SimpleSQLParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#SimpleCondition.
    def exitSimpleCondition(self, ctx:SimpleSQLParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#JoinCondition.
    def enterJoinCondition(self, ctx:SimpleSQLParser.JoinConditionContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#JoinCondition.
    def exitJoinCondition(self, ctx:SimpleSQLParser.JoinConditionContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#operator.
    def enterOperator(self, ctx:SimpleSQLParser.OperatorContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#operator.
    def exitOperator(self, ctx:SimpleSQLParser.OperatorContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#value.
    def enterValue(self, ctx:SimpleSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#value.
    def exitValue(self, ctx:SimpleSQLParser.ValueContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#limitClause.
    def enterLimitClause(self, ctx:SimpleSQLParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#limitClause.
    def exitLimitClause(self, ctx:SimpleSQLParser.LimitClauseContext):
        pass



del SimpleSQLParser