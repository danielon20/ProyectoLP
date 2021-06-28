import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
import ply.yacc as yacc

import lexi

lexer = lexi.goLexer()

from lexi import tokens


def p_coddigo(p):
    '''codigo : impresion COLON
              | impresion
              | expression COLON
              | expression
              | cicloFor
              | comparison
              | logic_operation
              | decVar COLON
              | decVar
              | funciones
              | agrupaciones
              | SenIF
              | SenStruct'''


###D
def p_for(p):
    '''cicloFor : FOR LLLAVE codigo RLLAVE
                | FOR comparison LLLAVE codigo RLLAVE
                | FOR logic_operation LLLAVE codigo RLLAVE
                | FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE
       incre    : ID INCREASE
                | ID DECREASE'''
#Pueden existir mas formas de incremento

#Aqui hay que poner las estructuras que se vayan creando
def p_decVar(p):
    '''decVar : decVarOne
              | VAR ID EQUAL INTEGER
              | VAR ID EQUAL ID
              | VAR ID EQUAL FLOAT
              | VAR ID EQUAL expression
              | VAR ID EQUAL logic_operation
              | VAR ID EQUAL comparison
              | sliceC
              | VAR ID EQUAL STRING
              | ID DEQUAL STRING
              | ID DEQUAL FLOAT
              | ID DEQUAL expression
              | ID DEQUAL logic_operation
              | ID DEQUAL comparison'''




def p_sliceC(p):
    '''sliceC : VAR ID LCORCHE RCORCHE type
              | ID DEQUAL funM
              | ID DEQUAL LCORCHE RCORCHE type agrupaciones
       funM : MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER RPAREN
            | MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER COMA INTEGER RPAREN
       type : INT32
            | INT64
            | FLOAT32
            | FLOAT64
            | BYTE
            | WINT
            | WFLOAT
            | WSTRING'''
#Mefalta int y string
#Tambien deberia estar solo el int si nada a lado, de igual manera el float
#Tambien debe considerarse valores booleanos (TRUE Y FALSE)

#Esto puede ser usado para quien le toque el array porque es un poco similar al slice
def p_agrupaciones(p):
    '''agrupaciones : LLLAVE INTEGER RLLAVE
                    | LLLAVE INTEGER enteros RLLAVE
                    | LLLAVE FLOAT RLLAVE
                    | LLLAVE FLOAT flotantes RLLAVE
                    | LLLAVE STRING RLLAVE
                    | LLLAVE STRING palabras RLLAVE
       enteros   : COMA INTEGER
                 | COMA INTEGER enteros
       flotantes : COMA FLOAT
                 | COMA FLOAT flotantes
       palabras  : COMA STRING
                 | COMA STRING palabras'''
        



def p_funciones(p):
    '''funciones : APPEND LPAREN ID COMA INTEGER RPAREN
                 | APPEND LPAREN ID COMA FLOAT RPAREN
                 | APPEND LPAREN ID COMA STRING RPAREN
                 | APPEND LPAREN ID COMA ID RPAREN
                 | LEN LPAREN ID RPAREN
                 | COPY LPAREN ID COMA ID RPAREN'''

def p_decVarOne(p):
    '''decVarOne : ID DEQUAL ID
                 | ID DEQUAL INTEGER'''


###D

###C
def p_if(p):
    'SenIF : IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE'

def p_struct(p):
    '''SenStruct : TYPE ID STRUCT LLLAVE declaration RLLAVE
    
       declaration : tipo variable
        
       tipo        : INT32
                   | INT64
                   | FLOAT32
                   | FLOAT64
                   | WSTRING
                   | BOOL
       
       variable    : ID'''
###C

###H
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
                       | ID

       negation        : NOT comparison
                       | NOT ID
                       
       logic_op        : AND
                       | OR'''
###H
    
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
