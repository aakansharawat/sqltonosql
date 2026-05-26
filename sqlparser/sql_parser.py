"""
parser.py
Main SQL parser using ANTLR4 generated lexer and parser.
"""

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Import ANTLR4 generated files
# These will be generated after running ANTLR4 on SimpleSQL.g4
try:
    from .generated.SimpleSQLLexer import SimpleSQLLexer
    from .generated.SimpleSQLParser import SimpleSQLParser
except ImportError:
    print("ERROR: Parser not generated yet!")
    print("Please run: antlr4 -Dlanguage=Python3 -o parser/generated parser/grammar/SimpleSQL.g4")
    sys.exit(1)


class SQLSyntaxError(Exception):
    """Custom exception for SQL syntax errors"""
    pass


class SQLErrorListener(ErrorListener):
    """
    Custom error listener to catch and report syntax errors
    """
    def __init__(self):
        super(SQLErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Called when ANTLR4 encounters a syntax error
        """
        error_msg = f"Syntax Error at line {line}, column {column}: {msg}"
        self.errors.append(error_msg)
        print(f" {error_msg}")


class SQLParser:
    """
    Main SQL Parser class
    Converts SQL query string into ANTLR4 parse tree
    """
    
    def __init__(self):
        """Initialize the parser"""
        self.error_listener = SQLErrorListener()
    
    def parse(self, sql_query):
        """
        Parse SQL query and return parse tree
        
        Args:
            sql_query (str): SQL query string
            
        Returns:
            ParseTree: ANTLR4 parse tree
            
        Raises:
            SQLSyntaxError: If SQL has syntax errors
        """
        print(f"📝 Parsing SQL: {sql_query}")
        
        # Step 1: Create input stream from SQL string
        input_stream = InputStream(sql_query)
        
        # Step 2: Create lexer (tokenize the input)
        lexer = SimpleSQLLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(self.error_listener)
        
        # Step 3: Create token stream from lexer
        token_stream = CommonTokenStream(lexer)
        
        # Step 4: Create parser from token stream
        parser = SimpleSQLParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)
        
        # Step 5: Parse the SQL statement
        # sqlStatement is the entry rule in our grammar
        parse_tree = parser.sqlStatement()
        
        # Step 6: Check for errors
        if self.error_listener.errors:
            error_msg = "\n".join(self.error_listener.errors)
            raise SQLSyntaxError(f"Failed to parse SQL:\n{error_msg}")
        
        print("✅ Parsing successful!")
        return parse_tree
    
    def parse_file(self, filename):
        """
        Parse SQL from a file
        
        Args:
            filename (str): Path to SQL file
            
        Returns:
            ParseTree: ANTLR4 parse tree
        """
        print(f"📂 Reading SQL from file: {filename}")
        
        try:
            with open(filename, 'r') as f:
                sql_query = f.read().strip()
            return self.parse(sql_query)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")


# Test the parser directly
if __name__ == "__main__":
    print("=" * 60)
    print("SQL Parser Test")
    print("=" * 60)
    
    # Test queries
    test_queries = [
        "SELECT name FROM users WHERE age > 25;",
        "SELECT * FROM products LIMIT 10;",
        "SELECT users.name, orders.total FROM users JOIN orders ON users.id = orders.user_id;",
    ]
    
    parser = SQLParser()
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Test {i} ---")
        try:
            tree = parser.parse(query)
            print(f"Parse tree: {tree.toStringTree(recog=SimpleSQLParser)}\n")
        except SQLSyntaxError as e:
            print(f"Error: {e}\n")
    
    print("=" * 60)
