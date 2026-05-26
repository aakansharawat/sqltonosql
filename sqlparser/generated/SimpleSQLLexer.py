# Generated from sql_parser/grammar/SimpleSQL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u00a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21x\n\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\7\26\u0084\n")
        buf.write("\26\f\26\16\26\u0087\13\26\3\27\6\27\u008a\n\27\r\27\16")
        buf.write("\27\u008b\3\30\3\30\7\30\u0090\n\30\f\30\16\30\u0093\13")
        buf.write("\30\3\30\3\30\3\31\6\31\u0098\n\31\r\31\16\31\u0099\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\7\32\u00a2\n\32\f\32\16\32")
        buf.write("\u00a5\13\32\3\32\3\32\2\2\33\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\3\2\32\4\2U")
        buf.write("Uuu\4\2GGgg\4\2NNnn\4\2EEee\4\2VVvv\4\2HHhh\4\2TTtt\4")
        buf.write("\2QQqq\4\2OOoo\4\2YYyy\4\2JJjj\4\2LLll\4\2KKkk\4\2PPp")
        buf.write("p\4\2FFff\4\2DDdd\4\2[[{{\4\2CCcc\5\2C\\aac|\6\2\62;C")
        buf.write("\\aac|\3\2\62;\3\2))\5\2\13\f\17\17\"\"\4\2\f\f\17\17")
        buf.write("\2\u00ad\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\3\65\3")
        buf.write("\2\2\2\5<\3\2\2\2\7A\3\2\2\2\tG\3\2\2\2\13L\3\2\2\2\r")
        buf.write("O\3\2\2\2\17U\3\2\2\2\21X\3\2\2\2\23\\\3\2\2\2\25a\3\2")
        buf.write("\2\2\27g\3\2\2\2\31i\3\2\2\2\33k\3\2\2\2\35m\3\2\2\2\37")
        buf.write("p\3\2\2\2!w\3\2\2\2#y\3\2\2\2%{\3\2\2\2\'}\3\2\2\2)\177")
        buf.write("\3\2\2\2+\u0081\3\2\2\2-\u0089\3\2\2\2/\u008d\3\2\2\2")
        buf.write("\61\u0097\3\2\2\2\63\u009d\3\2\2\2\65\66\t\2\2\2\66\67")
        buf.write("\t\3\2\2\678\t\4\2\289\t\3\2\29:\t\5\2\2:;\t\6\2\2;\4")
        buf.write("\3\2\2\2<=\t\7\2\2=>\t\b\2\2>?\t\t\2\2?@\t\n\2\2@\6\3")
        buf.write("\2\2\2AB\t\13\2\2BC\t\f\2\2CD\t\3\2\2DE\t\b\2\2EF\t\3")
        buf.write("\2\2F\b\3\2\2\2GH\t\r\2\2HI\t\t\2\2IJ\t\16\2\2JK\t\17")
        buf.write("\2\2K\n\3\2\2\2LM\t\t\2\2MN\t\17\2\2N\f\3\2\2\2OP\t\t")
        buf.write("\2\2PQ\t\b\2\2QR\t\20\2\2RS\t\3\2\2ST\t\b\2\2T\16\3\2")
        buf.write("\2\2UV\t\21\2\2VW\t\22\2\2W\20\3\2\2\2XY\t\23\2\2YZ\t")
        buf.write("\2\2\2Z[\t\5\2\2[\22\3\2\2\2\\]\t\20\2\2]^\t\3\2\2^_\t")
        buf.write("\2\2\2_`\t\5\2\2`\24\3\2\2\2ab\t\4\2\2bc\t\16\2\2cd\t")
        buf.write("\n\2\2de\t\16\2\2ef\t\6\2\2f\26\3\2\2\2gh\7?\2\2h\30\3")
        buf.write("\2\2\2ij\7@\2\2j\32\3\2\2\2kl\7>\2\2l\34\3\2\2\2mn\7@")
        buf.write("\2\2no\7?\2\2o\36\3\2\2\2pq\7>\2\2qr\7?\2\2r \3\2\2\2")
        buf.write("st\7#\2\2tx\7?\2\2uv\7>\2\2vx\7@\2\2ws\3\2\2\2wu\3\2\2")
        buf.write("\2x\"\3\2\2\2yz\7,\2\2z$\3\2\2\2{|\7.\2\2|&\3\2\2\2}~")
        buf.write("\7\60\2\2~(\3\2\2\2\177\u0080\7=\2\2\u0080*\3\2\2\2\u0081")
        buf.write("\u0085\t\24\2\2\u0082\u0084\t\25\2\2\u0083\u0082\3\2\2")
        buf.write("\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086,\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u008a")
        buf.write("\t\26\2\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c.\3\2\2\2\u008d")
        buf.write("\u0091\7)\2\2\u008e\u0090\n\27\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095")
        buf.write("\7)\2\2\u0095\60\3\2\2\2\u0096\u0098\t\30\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b\31\2")
        buf.write("\2\u009c\62\3\2\2\2\u009d\u009e\7/\2\2\u009e\u009f\7/")
        buf.write("\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\n\31\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a7\b\32\2\2\u00a7\64\3\2\2\2\t\2w\u0085\u008b")
        buf.write("\u0091\u0099\u00a3\3\b\2\2")
        return buf.getvalue()


class SimpleSQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SELECT = 1
    FROM = 2
    WHERE = 3
    JOIN = 4
    ON = 5
    ORDER = 6
    BY = 7
    ASC = 8
    DESC = 9
    LIMIT = 10
    EQUALS = 11
    GT = 12
    LT = 13
    GTE = 14
    LTE = 15
    NOT_EQUALS = 16
    STAR = 17
    COMMA = 18
    DOT = 19
    SEMICOLON = 20
    IDENTIFIER = 21
    NUMBER = 22
    STRING = 23
    WS = 24
    COMMENT = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'>'", "'<'", "'>='", "'<='", "'*'", "','", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "WHERE", "JOIN", "ON", "ORDER", "BY", "ASC", 
            "DESC", "LIMIT", "EQUALS", "GT", "LT", "GTE", "LTE", "NOT_EQUALS", 
            "STAR", "COMMA", "DOT", "SEMICOLON", "IDENTIFIER", "NUMBER", 
            "STRING", "WS", "COMMENT" ]

    ruleNames = [ "SELECT", "FROM", "WHERE", "JOIN", "ON", "ORDER", "BY", 
                  "ASC", "DESC", "LIMIT", "EQUALS", "GT", "LT", "GTE", "LTE", 
                  "NOT_EQUALS", "STAR", "COMMA", "DOT", "SEMICOLON", "IDENTIFIER", 
                  "NUMBER", "STRING", "WS", "COMMENT" ]

    grammarFileName = "SimpleSQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


