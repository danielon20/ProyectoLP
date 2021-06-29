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

              | scan_func COLON
              | scan_func

              | expression COLON
              | expression

              | cicloFor

              | comparison

              | logic_operation

              | decVar COLON
              | decVar

              | var_asignation
              | var_asignation COLON

              | funciones
              | funciones COLON

              | SenIF

              | SenStruct
              | cStruct

              | switch_statement

              | array_declaration COLON
              | array_declaration
              | array_var COLON
              | array_var
              | array_assignment COLON
              | array_assignment

              | slice_declaration COLON
              | slice_declaration
              | slice_var COLON
              | slice_var
              | slice_assignment COLON
              | slice_assignment
              
              | map_declaration COLON
              | map_declaration
              | map_assignment COLON
              | map_assignment
              
              | func_declaration
              
              | main_func'''

def p_values(p):
    '''values : STRING
              | INTEGER
              | FLOAT
              | TRUE
              | FALSE'''
              
def p_data_types(p):
    '''data_types : INT32
            | INT64
            | FLOAT32
            | FLOAT64
            | BYTE
            | WINT
            | WFLOAT
            | WSTRING
            | BOOL'''

def p_operations(p):
    '''operations : expression 
                  | comparison 
                  | logic_operation'''

def p_data_structure(p):
    '''data_structure : array_var
                      | map_var'''

def p_var_asignation(p):
    '''var_asignation : ID EQUAL any
                any : values
                      | operations
                      | ID
                      | data_structure
                      | funciones'''

def p_arr_content(p): 
    '''arr_content :  LLLAVE items COMA more_items RLLAVE
                | LLLAVE items RLLAVE
                
        more_items : items COMA more_items
                   | items
                   
             items : values
                   | operations'''

def p_something(p):
    '''something : ID 
                 | data_structure
                 | values
                 | operations'''

def p_main_func(p):
    '''main_func : FUNC MAIN LPAREN RPAREN LLLAVE codigo RLLAVE'''

def p_scan_func(p):
    '''scan_func : SCAN LPAREN POINTER RPAREN'''



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
              | VAR ID EQUAL STRING
              | ID DEQUAL STRING
              | ID DEQUAL FLOAT
              | ID DEQUAL expression
              | ID DEQUAL logic_operation
              | ID DEQUAL comparison'''


###Slices
def p_slice_declaration(p):
    '''slice_declaration : VAR ID LCORCHE RCORCHE data_types
                         | VAR ID EQUAL LCORCHE RCORCHE data_types arr_content
                         | VAR ID EQUAL funM
                         | ID DEQUAL funM
                         | ID DEQUAL LCORCHE RCORCHE data_types arr_content


                    funM : MAKE LPAREN LCORCHE RCORCHE data_types COMA cap RPAREN
                         | MAKE LPAREN LCORCHE RCORCHE data_types COMA cap COMA cap RPAREN
                         
                     cap : INTEGER
                         | ID
                         | expression'''

def p_slice_var(p):
    '''slice_var : ID LCORCHE index_s RCORCHE
         
         index_s : ID
                 | INTEGER
                 | expression'''

def p_slice_assignment(p):
    '''slice_assignment : slice_var EQUAL something_s
    
              something_s : ID 
                        | array_var
                        | values
                        | operations'''

####


def p_funciones(p):
    '''funciones : APPEND LPAREN ID COMA values RPAREN
                 | APPEND LPAREN ID COMA ID RPAREN
                 | LEN LPAREN ID RPAREN
                 | COPY LPAREN ID COMA ID RPAREN
                 | DELETE LPAREN ID COMA ID RPAREN'''

def p_decVarOne(p):
    '''decVarOne : ID DEQUAL ID
                 | ID DEQUAL INTEGER'''


###D

###C
def p_if(p):
    '''SenIF : IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE
             | IF LPAREN TRUE RPAREN LLLAVE codigo RLLAVE
             | IF LPAREN FALSE RPAREN LLLAVE codigo RLLAVE'''

def p_struct(p):
    '''SenStruct : TYPE ID STRUCT LLLAVE declaration RLLAVE
    
       declaration : variable data_types
                   | declaration variable data_types
       
       variable    : ID'''

def p_createStruct(p):
    '''cStruct : ID DEQUAL ID LLLAVE asignaciones RLLAVE
    
       asignaciones : ID POINTS valor
                    | ID POINTS valor COMA asignaciones
       
       valor : ID
             | INTEGER
             | TRUE
             | FALSE'''
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
    '''logic_operation : logic_value logic_recu
                       | negation

       logic_recu      : logic_op logic_value
                       | logic_op logic_value logic_recu
        

       logic_value     : negation
                       | comparison
                       | ID

       negation        : NOT comparison
                       | NOT ID
                       
       logic_op        : AND
                       | OR'''

def p_switch(p):
    '''switch_statement : SWITCH ID LLLAVE cases RLLAVE

                  cases : CASE values POINTS codigo 
                        | CASE values POINTS codigo more

                  more : cases 
                       | DEFAULT POINTS codigo'''

def p_array_declaration(p):
    '''array_declaration : VAR ID LCORCHE capacity RCORCHE data_types
                         | VAR ID EQUAL LCORCHE capacity RCORCHE data_types arr_content

       capacity : INTEGER 
                | ID
                | expression'''

def p_array_var(p):
    '''array_var : ID LCORCHE index RCORCHE
         
           index : ID
                 | INTEGER
                 | expression'''

def p_array_assignment(p):
    '''array_assignment : array_var EQUAL something'''

def p_map_declaration(p):
    '''map_declaration : VAR ID LCORCHE data_types RCORCHE data_types'''

def p_map_var(p):
    '''map_var : ID LCORCHE key RCORCHE
           key : ID 
               | values
               | operations'''

def p_map_assignment(p):
    '''map_assignment : array_var EQUAL something'''

def p_func_declaration(p):
    '''func_declaration : FUNC ID LPAREN params RPAREN data_types LLLAVE codigo RETURN retorno RLLAVE
                        | FUNC ID LPAREN params RPAREN data_types LLLAVE RETURN return_value RLLAVE

                return_value : retorno COLON
                             | retorno
                
                retorno : ID 
                        | values
                        | operations
                        | data_structure
                        
                params : ID data_types 
                       | more_params
                       
                more_params : ID data_types COMA params'''


###H
    
def p_impresion(p):
    '''impresion : PRINT LPAREN content RPAREN
         content : values
                 | operations
                 | funciones
                 | data_structure
                 | ID'''



def p_expression(p):
    '''expression : something_ex
                  | something_ex adicionaEx

       adicionaEx : op something_ex
                  | op something_ex adicionaEx

    something_ex : ID
                 | INTEGER
                 | FLOAT
                 | data_structure
                 | funciones

              op : PLUS
                 | TIMES
                 | DIVIDE
                 | MINUS'''
    


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
