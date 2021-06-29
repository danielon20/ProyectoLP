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
              | SenElseIF
              | SenElse

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
    
###Daniel Viscarra - Inicio
def p_something(p):
    '''something : ID 
                 | data_structure
                 | values
                 | operations'''

def p_main_func(p):
    '''main_func : FUNC MAIN LPAREN RPAREN LLLAVE codigo RLLAVE'''

def p_scan_func(p):
    '''scan_func : SCAN LPAREN POINTER RPAREN'''




def p_for(p):
    '''cicloFor : FOR LLLAVE codigo RLLAVE
                | FOR comparison LLLAVE codigo RLLAVE
                | FOR logic_operation LLLAVE codigo RLLAVE
                | FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE
       incre    : ID INCREASE
                | ID DECREASE'''

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

###Daniel Viscarra - Fin

###Carlos Quiñonez - Inicio
def p_funciones(p):
    '''funciones : APPEND LPAREN ID COMA values RPAREN
                 | APPEND LPAREN ID COMA ID RPAREN
                 | LEN LPAREN ID RPAREN
                 | COPY LPAREN ID COMA ID RPAREN
                 | DELETE LPAREN ID COMA ID RPAREN'''

def p_decVarOne(p):
    '''decVarOne : ID DEQUAL ID
                 | ID DEQUAL INTEGER'''


def p_if(p):
    '''SenIF : IF comparison LLLAVE codigo RLLAVE
             | IF TRUE LLLAVE codigo RLLAVE
             | IF FALSE LLLAVE codigo RLLAVE'''

def p_elseif(p):
    '''SenElseIF : ELSE IF comparison LLLAVE codigo RLLAVE
             | ELSE IF TRUE LLLAVE codigo RLLAVE
             | ELSE IF FALSE LLLAVE codigo RLLAVE'''

def p_else(p):
    '''SenElse : ELSE LLLAVE codigo RLLAVE'''

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
###Carlos Quiñonez - Fin
    
###Hector Villegas - Inicio
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
    
###Hector Villegas - Fin

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    
# Build the parser
parser = yacc.yacc()
 
ListaDeclaraciones = ['var x = 4','a := 5', 'var jho = 4.5', 'saludo := "Hola"']
ListaExpresiones = ['5+4','9*4/4','var4+var5','x>4','y<5','x>4 && y<5 && z>4']
ListaEstructuras = ['var arra = [5]int {4,5,6}', 'var arra2 [4] float','type persona struct { nombre string edad int }','var sli [] string','var map_capitales[string]string']
ListaMetodos = ['len (lista1)','copy (arr2, arr3)','delete(slic,var5)','append(listapalabras,"suiza")']
ListaFunciones = ['func sum(x int, y int) int {return x + y;}','func mul(x int, y int) int {return x * y;}']
ListaControl = ['for i<4 { print(var4) }','switch x{ case 1: print(1); default: print(0);}','if a>5 { print(var1) }']
print('**Algoritmo de prueba**')
print('******************************')
print('Declaraciones')
for pal in ListaDeclaraciones:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")

print('******************************')
print('Expresiones')
for pal in ListaExpresiones:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")
        
print('******************************')        
print('Estructura datos')
for pal in ListaEstructuras:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")
        
print('******************************')
print('Metodos')
for pal in ListaMetodos:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")

print('******************************')
print('Funciones')
for pal in ListaFunciones:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")

print('******************************')
print('Estructuras de control')
for pal in ListaControl:
    result = parser.parse(pal)
    if result is None:
        print('Linea Evaluada')
        print(pal)
        print("Resultado: Its OK!")
    else:
        print("Resultado: Error de sintaxis :(")
