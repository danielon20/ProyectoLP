import ply.lex as lex

# CARLOS QUINONEZ
# INICIO

#palabras reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'case' : 'CASE',
    'switch' : 'SWITCH',
    'for' : 'FOR',
    'package' : 'PACKAGE',
    'main' : 'MAIN',
    'map' : 'MAP',
    'print' : 'PRINT',
    'func' : 'FUNC',
    'array' : 'ARRAY',
    'len' : 'LEN',
    'const' : 'CONST',
    'join' : 'JOIN',
    'cap' : 'CAP',
    'make' : 'MAKE',
    'append' : 'APPEND',
    'copy' : 'COPY',
    'var' : 'VAR',
    'type' : 'TYPE',
    'struct' : 'STRUCT',
    'interface' : 'INTERFACE',
    'int32' : 'INT32',
    'int64' : 'INT64',
    'byte' : 'BYTE',
    'float32' : 'FLOAT32',
    'float64' : 'FLOAT64',
    'true' : 'TRUE',
    'false' : "FALSE",
    'bool' : 'BOOL',
    'print' : "PRINT",
    'scan' : 'SCAN'
}

#list of tokens
tokens = [
    'ID',  
    'STRING',
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'INCREASE', 
    'DECREASE',
    'EQUAL_COMPARE',
    'GREATER',
    'SMALLER',
    'GREATER_OR_EQUAL',
    'SMALLER_OR_EQUAL',
    'NOT_EQUAL',
    'AND',
    'OR',
    'NOT',
    'EQUAL',
    'DEQUAL',
    'LPAREN',
    'RPAREN',
    'LCORCHE',

# FIN

# HECTOR VILLEGAS
# INICIO

    'RCORCHE',
    'LLLAVE',
    'RLLAVE',
    'COMMENT',
    'MULTI_COMMENT',
    'POINTER',
    'COMA',
    'COLON'
] +  list(reserved.values())

def goLexer():  
    #rules

    t_STRING  = r'\".*\"'
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_MOD     = r'%'
    t_INCREASE = r'\+\+'
    t_DECREASE = r'--'
    t_EQUAL_COMPARE = r'=='
    t_GREATER = r'>'
    t_SMALLER = r'<'
    t_GREATER_OR_EQUAL = r'>='
    t_SMALLER_OR_EQUAL = r'<='
    t_NOT_EQUAL = r'!='
    t_AND       = r'&&'       
    t_OR        = r'\|\|'
    t_NOT     = r'!'
    t_EQUAL   = r'='
    t_DEQUAL = r':='
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LCORCHE = r'\['
    t_RCORCHE = r'\]'
    t_LLLAVE = r'\{'
    t_RLLAVE = r'\}'
    t_COMA = r','
    t_COLON = r';'

# FIN
# DANIEL VISCARRA
# INICIO

    t_ignore = ' \t'
    t_ignore_COMMENT = r'//.*'
    t_ignore_MULTI_COMMENT = r'/\*\n*.*\n*\*/'
    

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'ID')    # Check for reserved words
        return t

    def t_POINTER(t):
        r'[& | *][a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'POINTER') #Check for reserved words
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_FLOAT(t):
        r'([0-9] | [1-9][0-9]+)\.\d+'
        t.value = float(t.value)    
        return t

    def t_INTEGER(t):
        r'[0-9] | [1-9][0-9]+'
        t.value = int(t.value)    
        return t

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    return lex.lex()

# FIN
