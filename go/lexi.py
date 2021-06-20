import ply.lex as lex

#list of tokens

tokens = (
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
    'LPAREN',
    'RPAREN',
    'LCORCHE',
    'RCORCHE',
    'LLLAVE',
    'RLLAVE'
)

#rules

t_ID      = r'[aA-zZ][aA-zZ0-9_\-]*'
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
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCORCHE = r'\['
t_RCORCHE = r'\]'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = 'class95_x-4=123.5'
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
