// SimpleSQL.g4
// ANTLR4 Grammar for Basic SQL Parsing
// Supports: SELECT, FROM, WHERE, JOIN, ORDER BY, LIMIT

grammar SimpleSQL;

// ========================================
// PARSER RULES (start with lowercase)
// ========================================

// Entry point - a complete SQL statement
sqlStatement
    : selectStatement EOF
    ;

// SELECT statement
selectStatement
    : SELECT columnList 
      FROM tableName 
      joinClause*
      whereClause? 
      orderByClause?
      limitClause?
      SEMICOLON?
    ;

// Column list: column1, column2, ... or *
columnList
    : STAR                                    # SelectAll
    | columnName (COMMA columnName)*          # SelectColumns
    ;

// Column name (can be table.column or just column)
columnName
    : (IDENTIFIER DOT)? IDENTIFIER
    ;

// Table name
tableName
    : IDENTIFIER
    ;

// JOIN clause
joinClause
    : JOIN tableName ON condition
    ;

// WHERE clause
whereClause
    : WHERE condition
    ;

// ORDER BY clause
orderByClause
    : ORDER BY orderByItem (COMMA orderByItem)*
    ;

// ORDER BY item (column with ASC/DESC)
orderByItem
    : columnName (ASC | DESC)?
    ;

// Condition (e.g., age > 25, name = 'John')
condition
    : columnName operator value              # SimpleCondition
    | columnName EQUALS columnName           # JoinCondition
    ;

// Operators
operator
    : EQUALS
    | GT
    | LT
    | GTE
    | LTE
    | NOT_EQUALS
    ;

// Values (numbers or strings)
value
    : NUMBER
    | STRING
    ;

// LIMIT clause
limitClause
    : LIMIT NUMBER
    ;

// ========================================
// LEXER RULES (start with UPPERCASE)
// ========================================

// Keywords
SELECT      : [Ss][Ee][Ll][Ee][Cc][Tt];
FROM        : [Ff][Rr][Oo][Mm];
WHERE       : [Ww][Hh][Ee][Rr][Ee];
JOIN        : [Jj][Oo][Ii][Nn];
ON          : [Oo][Nn];
ORDER       : [Oo][Rr][Dd][Ee][Rr];
BY          : [Bb][Yy];
ASC         : [Aa][Ss][Cc];
DESC        : [Dd][Ee][Ss][Cc];
LIMIT       : [Ll][Ii][Mm][Ii][Tt];

// Operators
EQUALS      : '=';
GT          : '>';
LT          : '<';
GTE         : '>=';
LTE         : '<=';
NOT_EQUALS  : '!=' | '<>';

// Symbols
STAR        : '*';
COMMA       : ',';
DOT         : '.';
SEMICOLON   : ';';

// Identifiers (table names, column names)
IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

// Numbers
NUMBER
    : [0-9]+
    ;

// Strings (single quotes)
STRING
    : '\'' (~'\'')* '\''
    ;

// Whitespace (ignore)
WS
    : [ \t\r\n]+ -> skip
    ;

// Comments (ignore)
COMMENT
    : '--' ~[\r\n]* -> skip
    ;
