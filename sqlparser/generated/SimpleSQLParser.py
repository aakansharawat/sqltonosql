# Generated from sql_parser/grammar/SimpleSQL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3%\n\3\f\3\16\3")
        buf.write("(\13\3\3\3\5\3+\n\3\3\3\5\3.\n\3\3\3\5\3\61\n\3\3\3\5")
        buf.write("\3\64\n\3\3\4\3\4\3\4\3\4\7\4:\n\4\f\4\16\4=\13\4\5\4")
        buf.write("?\n\4\3\5\3\5\5\5C\n\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7\tV\n\t\f\t\16\t")
        buf.write("Y\13\t\3\n\3\n\5\n]\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13g\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\5\3\2\n")
        buf.write("\13\3\2\r\22\3\2\30\31\2m\2\34\3\2\2\2\4\37\3\2\2\2\6")
        buf.write(">\3\2\2\2\bB\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16M\3\2\2\2")
        buf.write("\20P\3\2\2\2\22Z\3\2\2\2\24f\3\2\2\2\26h\3\2\2\2\30j\3")
        buf.write("\2\2\2\32l\3\2\2\2\34\35\5\4\3\2\35\36\7\2\2\3\36\3\3")
        buf.write("\2\2\2\37 \7\3\2\2 !\5\6\4\2!\"\7\4\2\2\"&\5\n\6\2#%\5")
        buf.write("\f\7\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'*\3\2")
        buf.write("\2\2(&\3\2\2\2)+\5\16\b\2*)\3\2\2\2*+\3\2\2\2+-\3\2\2")
        buf.write("\2,.\5\20\t\2-,\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\61\5\32")
        buf.write("\16\2\60/\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\64\7")
        buf.write("\26\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\5\3\2\2\2\65?\7")
        buf.write("\23\2\2\66;\5\b\5\2\678\7\24\2\28:\5\b\5\29\67\3\2\2\2")
        buf.write(":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<?\3\2\2\2=;\3\2\2\2>\65")
        buf.write("\3\2\2\2>\66\3\2\2\2?\7\3\2\2\2@A\7\27\2\2AC\7\25\2\2")
        buf.write("B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\7\27\2\2E\t\3\2\2\2F")
        buf.write("G\7\27\2\2G\13\3\2\2\2HI\7\6\2\2IJ\5\n\6\2JK\7\7\2\2K")
        buf.write("L\5\24\13\2L\r\3\2\2\2MN\7\5\2\2NO\5\24\13\2O\17\3\2\2")
        buf.write("\2PQ\7\b\2\2QR\7\t\2\2RW\5\22\n\2ST\7\24\2\2TV\5\22\n")
        buf.write("\2US\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\21\3\2\2\2")
        buf.write("YW\3\2\2\2Z\\\5\b\5\2[]\t\2\2\2\\[\3\2\2\2\\]\3\2\2\2")
        buf.write("]\23\3\2\2\2^_\5\b\5\2_`\5\26\f\2`a\5\30\r\2ag\3\2\2\2")
        buf.write("bc\5\b\5\2cd\7\r\2\2de\5\b\5\2eg\3\2\2\2f^\3\2\2\2fb\3")
        buf.write("\2\2\2g\25\3\2\2\2hi\t\3\2\2i\27\3\2\2\2jk\t\4\2\2k\31")
        buf.write("\3\2\2\2lm\7\f\2\2mn\7\30\2\2n\33\3\2\2\2\r&*-\60\63;")
        buf.write(">BW\\f")
        return buf.getvalue()


class SimpleSQLParser ( Parser ):

    grammarFileName = "SimpleSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'>'", 
                     "'<'", "'>='", "'<='", "<INVALID>", "'*'", "','", "'.'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "JOIN", "ON", 
                      "ORDER", "BY", "ASC", "DESC", "LIMIT", "EQUALS", "GT", 
                      "LT", "GTE", "LTE", "NOT_EQUALS", "STAR", "COMMA", 
                      "DOT", "SEMICOLON", "IDENTIFIER", "NUMBER", "STRING", 
                      "WS", "COMMENT" ]

    RULE_sqlStatement = 0
    RULE_selectStatement = 1
    RULE_columnList = 2
    RULE_columnName = 3
    RULE_tableName = 4
    RULE_joinClause = 5
    RULE_whereClause = 6
    RULE_orderByClause = 7
    RULE_orderByItem = 8
    RULE_condition = 9
    RULE_operator = 10
    RULE_value = 11
    RULE_limitClause = 12

    ruleNames =  [ "sqlStatement", "selectStatement", "columnList", "columnName", 
                   "tableName", "joinClause", "whereClause", "orderByClause", 
                   "orderByItem", "condition", "operator", "value", "limitClause" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    JOIN=4
    ON=5
    ORDER=6
    BY=7
    ASC=8
    DESC=9
    LIMIT=10
    EQUALS=11
    GT=12
    LT=13
    GTE=14
    LTE=15
    NOT_EQUALS=16
    STAR=17
    COMMA=18
    DOT=19
    SEMICOLON=20
    IDENTIFIER=21
    NUMBER=22
    STRING=23
    WS=24
    COMMENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SqlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStatement(self):
            return self.getTypedRuleContext(SimpleSQLParser.SelectStatementContext,0)


        def EOF(self):
            return self.getToken(SimpleSQLParser.EOF, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_sqlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlStatement" ):
                listener.enterSqlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlStatement" ):
                listener.exitSqlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlStatement" ):
                return visitor.visitSqlStatement(self)
            else:
                return visitor.visitChildren(self)




    def sqlStatement(self):

        localctx = SimpleSQLParser.SqlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sqlStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.selectStatement()
            self.state = 27
            self.match(SimpleSQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SimpleSQLParser.SELECT, 0)

        def columnList(self):
            return self.getTypedRuleContext(SimpleSQLParser.ColumnListContext,0)


        def FROM(self):
            return self.getToken(SimpleSQLParser.FROM, 0)

        def tableName(self):
            return self.getTypedRuleContext(SimpleSQLParser.TableNameContext,0)


        def joinClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleSQLParser.JoinClauseContext)
            else:
                return self.getTypedRuleContext(SimpleSQLParser.JoinClauseContext,i)


        def whereClause(self):
            return self.getTypedRuleContext(SimpleSQLParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(SimpleSQLParser.OrderByClauseContext,0)


        def limitClause(self):
            return self.getTypedRuleContext(SimpleSQLParser.LimitClauseContext,0)


        def SEMICOLON(self):
            return self.getToken(SimpleSQLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectStatement(self):

        localctx = SimpleSQLParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(SimpleSQLParser.SELECT)
            self.state = 30
            self.columnList()
            self.state = 31
            self.match(SimpleSQLParser.FROM)
            self.state = 32
            self.tableName()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimpleSQLParser.JOIN:
                self.state = 33
                self.joinClause()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleSQLParser.WHERE:
                self.state = 39
                self.whereClause()


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleSQLParser.ORDER:
                self.state = 42
                self.orderByClause()


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleSQLParser.LIMIT:
                self.state = 45
                self.limitClause()


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleSQLParser.SEMICOLON:
                self.state = 48
                self.match(SimpleSQLParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_columnList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectColumnsContext(ColumnListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleSQLParser.ColumnListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleSQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(SimpleSQLParser.ColumnNameContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleSQLParser.COMMA)
            else:
                return self.getToken(SimpleSQLParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectColumns" ):
                listener.enterSelectColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectColumns" ):
                listener.exitSelectColumns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectColumns" ):
                return visitor.visitSelectColumns(self)
            else:
                return visitor.visitChildren(self)


    class SelectAllContext(ColumnListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleSQLParser.ColumnListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(SimpleSQLParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectAll" ):
                listener.enterSelectAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectAll" ):
                listener.exitSelectAll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectAll" ):
                return visitor.visitSelectAll(self)
            else:
                return visitor.visitChildren(self)



    def columnList(self):

        localctx = SimpleSQLParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleSQLParser.STAR]:
                localctx = SimpleSQLParser.SelectAllContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(SimpleSQLParser.STAR)
                pass
            elif token in [SimpleSQLParser.IDENTIFIER]:
                localctx = SimpleSQLParser.SelectColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.columnName()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimpleSQLParser.COMMA:
                    self.state = 53
                    self.match(SimpleSQLParser.COMMA)
                    self.state = 54
                    self.columnName()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleSQLParser.IDENTIFIER)
            else:
                return self.getToken(SimpleSQLParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(SimpleSQLParser.DOT, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = SimpleSQLParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 62
                self.match(SimpleSQLParser.IDENTIFIER)
                self.state = 63
                self.match(SimpleSQLParser.DOT)


            self.state = 66
            self.match(SimpleSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SimpleSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = SimpleSQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SimpleSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(SimpleSQLParser.JOIN, 0)

        def tableName(self):
            return self.getTypedRuleContext(SimpleSQLParser.TableNameContext,0)


        def ON(self):
            return self.getToken(SimpleSQLParser.ON, 0)

        def condition(self):
            return self.getTypedRuleContext(SimpleSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_joinClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinClause" ):
                listener.enterJoinClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinClause" ):
                listener.exitJoinClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoinClause" ):
                return visitor.visitJoinClause(self)
            else:
                return visitor.visitChildren(self)




    def joinClause(self):

        localctx = SimpleSQLParser.JoinClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_joinClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(SimpleSQLParser.JOIN)
            self.state = 71
            self.tableName()
            self.state = 72
            self.match(SimpleSQLParser.ON)
            self.state = 73
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SimpleSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SimpleSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = SimpleSQLParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SimpleSQLParser.WHERE)
            self.state = 76
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(SimpleSQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(SimpleSQLParser.BY, 0)

        def orderByItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleSQLParser.OrderByItemContext)
            else:
                return self.getTypedRuleContext(SimpleSQLParser.OrderByItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleSQLParser.COMMA)
            else:
                return self.getToken(SimpleSQLParser.COMMA, i)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByClause" ):
                return visitor.visitOrderByClause(self)
            else:
                return visitor.visitChildren(self)




    def orderByClause(self):

        localctx = SimpleSQLParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SimpleSQLParser.ORDER)
            self.state = 79
            self.match(SimpleSQLParser.BY)
            self.state = 80
            self.orderByItem()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimpleSQLParser.COMMA:
                self.state = 81
                self.match(SimpleSQLParser.COMMA)
                self.state = 82
                self.orderByItem()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(SimpleSQLParser.ColumnNameContext,0)


        def ASC(self):
            return self.getToken(SimpleSQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(SimpleSQLParser.DESC, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_orderByItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByItem" ):
                listener.enterOrderByItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByItem" ):
                listener.exitOrderByItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByItem" ):
                return visitor.visitOrderByItem(self)
            else:
                return visitor.visitChildren(self)




    def orderByItem(self):

        localctx = SimpleSQLParser.OrderByItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orderByItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.columnName()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleSQLParser.ASC or _la==SimpleSQLParser.DESC:
                self.state = 89
                _la = self._input.LA(1)
                if not(_la==SimpleSQLParser.ASC or _la==SimpleSQLParser.DESC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleSQLParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleSQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnName(self):
            return self.getTypedRuleContext(SimpleSQLParser.ColumnNameContext,0)

        def operator(self):
            return self.getTypedRuleContext(SimpleSQLParser.OperatorContext,0)

        def value(self):
            return self.getTypedRuleContext(SimpleSQLParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleCondition" ):
                listener.enterSimpleCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleCondition" ):
                listener.exitSimpleCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleCondition" ):
                return visitor.visitSimpleCondition(self)
            else:
                return visitor.visitChildren(self)


    class JoinConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleSQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleSQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(SimpleSQLParser.ColumnNameContext,i)

        def EQUALS(self):
            return self.getToken(SimpleSQLParser.EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinCondition" ):
                listener.enterJoinCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinCondition" ):
                listener.exitJoinCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoinCondition" ):
                return visitor.visitJoinCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = SimpleSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = SimpleSQLParser.SimpleConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.columnName()
                self.state = 93
                self.operator()
                self.state = 94
                self.value()
                pass

            elif la_ == 2:
                localctx = SimpleSQLParser.JoinConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.columnName()
                self.state = 97
                self.match(SimpleSQLParser.EQUALS)
                self.state = 98
                self.columnName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(SimpleSQLParser.EQUALS, 0)

        def GT(self):
            return self.getToken(SimpleSQLParser.GT, 0)

        def LT(self):
            return self.getToken(SimpleSQLParser.LT, 0)

        def GTE(self):
            return self.getToken(SimpleSQLParser.GTE, 0)

        def LTE(self):
            return self.getToken(SimpleSQLParser.LTE, 0)

        def NOT_EQUALS(self):
            return self.getToken(SimpleSQLParser.NOT_EQUALS, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = SimpleSQLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleSQLParser.EQUALS) | (1 << SimpleSQLParser.GT) | (1 << SimpleSQLParser.LT) | (1 << SimpleSQLParser.GTE) | (1 << SimpleSQLParser.LTE) | (1 << SimpleSQLParser.NOT_EQUALS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SimpleSQLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(SimpleSQLParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = SimpleSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==SimpleSQLParser.NUMBER or _la==SimpleSQLParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(SimpleSQLParser.LIMIT, 0)

        def NUMBER(self):
            return self.getToken(SimpleSQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return SimpleSQLParser.RULE_limitClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClause" ):
                listener.enterLimitClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClause" ):
                listener.exitLimitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitClause" ):
                return visitor.visitLimitClause(self)
            else:
                return visitor.visitChildren(self)




    def limitClause(self):

        localctx = SimpleSQLParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SimpleSQLParser.LIMIT)
            self.state = 107
            self.match(SimpleSQLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





