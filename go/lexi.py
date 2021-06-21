import ply.lex as lex

#palabras reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'switch' : 'SWITCH',
    'for' : 'FOR',
    'package' : 'PACKAGE',
    'main' : 'MAIN',
    'print' : 'PRINT',
    'func' : 'FUNC',
    'array' : 'ARRAY',
    'len' : 'LEN',
    'const' : 'CONST',
    'join' : 'JOIN',
    'var' : 'VAR',
    'type' : 'TYPE',
    'struct' : 'STRUCT'
    'interface' : 'INTERFACE'
}

#list of tokens
tokens = [
    'ID', 
    'BOOL', 
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
    'RCORCHE',
    'LLLAVE',
    'RLLAVE',
    'COMMENT',
    'MULTI_COMMENT',
    'POINTER',
    'STRUCT'
] +  list(reserved.values())

def goLexer():  
    #rules

    t_BOOL    = r'(true|false)'
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
    
    def t_STRUCT(t):
        r'type\s[a-zA-Z_]+\s struct\{ w* \}'
        t.type = reserved.get(t.value, 'STRUCT') #Check for reserved words
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_FLOAT(t):
        r'\d+\.\d+'
        t.value = float(t.value)    
        return t

    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    return lex.lex()
