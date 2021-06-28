import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
import ply.yacc as yacc

import lexi

lexer = lexi.goLexer()

from lexi import tokens

def p_coddigo(p):
    '''codigo : impresion
              | expression
              | cicloFor
              | comparison
              | logic_operation
              | SenIF
              | SenStruct'''



def p_for(p):
    'cicloFor : FOR LLLAVE codigo RLLAVE'

def p_comparison(p):
    '''comparison : value op value
       value      : ID
                  | expression
       op         : GREATER
                  | SMALLER
                  | GREATER_OR_EQUAL
                  | SMALLER_OR_EQUAL
                  | EQUAL_COMPARE
                  | NOT_EQUAL'''

def p_logic_operation(p):
    '''logic_operation : logic_value logic_op logic_value
                       | negation

       logic_value     : negation
                       | comparison

       negation        : NOT comparison
                       | NOT ID
                       
       logic_op        : AND
                       | OR'''


def p_if(p):
    'SenIF : IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE'

def p_struct(p):
    '''SenStruct : TYPE ID STRUCT LLLAVE declaration RLLAVE
    
       declaration : tipo variable
        
       tipo        : INT32
                   | INT64
                   | FLOAT32
                   | FLOAT64
                   | STRING
                   | BOOL
       
       variable    : ID'''

    
def p_impresion(p):
    'impresion : PRINT LPAREN expression RPAREN'



def p_expression_plus(p):
    'expression : expression PLUS term'
    
 
def p_expression_minus(p):
    'expression : expression MINUS term'
    
 
def p_expression_term(p):
    'expression : term'
    
 
def p_term_times(p):
    'term : term TIMES factor'
    
 
def p_term_div(p):
    'term : term DIVIDE factor'
    
 
def p_term_factor(p):
    'term : factor'
    
 
def p_factor_num(p):
    'factor : INTEGER'

def p_factor_id(p):
    'factor : ID'
    
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    
# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
