
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ARRAY BOOL BYTE CAP CASE COLON COMA COMMENT CONST COPY DECREASE DEFAULT DELETE DEQUAL DIVIDE ELSE EQUAL EQUAL_COMPARE FALSE FLOAT FLOAT32 FLOAT64 FOR FUNC GREATER GREATER_OR_EQUAL ID IF INCREASE INT32 INT64 INTEGER INTERFACE JOIN LCORCHE LEN LLLAVE LPAREN MAIN MAKE MAP MINUS MOD MULTI_COMMENT NOT NOT_EQUAL OR PACKAGE PLUS POINTER POINTS PRINT RCORCHE RETURN RLLAVE RPAREN SCAN SMALLER SMALLER_OR_EQUAL STRING STRUCT SWITCH TIMES TRUE TYPE VAR WFLOAT WINT WSTRINGcodigo : impresion COLON\n              | impresion\n\n              | expression COLON\n              | expression\n\n              | cicloFor\n\n              | comparison\n\n              | logic_operation\n\n              | decVar COLON\n              | decVar\n\n              | funciones\n              | funciones COLON\n\n              | SenIF\n\n              | SenStruct\n\n              | switch_statement\n\n              | array_declaration COLON\n              | array_declaration\n              | array_var COLON\n              | array_var\n              | array_assignment COLON\n              | array_assignment\n              \n              | map_declaration COLON\n              | map_declaration\n              | map_assignment COLON\n              | map_assignment\n              \n              | func_declarationvalues : STRING\n              | INTEGER\n              | FLOAT\n              | TRUE\n              | FALSEdata_types : INT32\n            | INT64\n            | FLOAT32\n            | FLOAT64\n            | BYTE\n            | WINT\n            | WFLOAT\n            | WSTRING\n            | BOOLoperations : expression \n                  | comparison \n                  | logic_operationdata_structure : array_var\n                      | map_vararr_content :  LLLAVE items COMA more_items RLLAVE\n                | LLLAVE items RLLAVE\n                \n        more_items : items COMA more_items\n                   | items\n                   \n             items : values\n                   | operationssomething : ID \n                 | data_structure\n                 | values\n                 | operationscicloFor : FOR LLLAVE codigo RLLAVE\n                | FOR comparison LLLAVE codigo RLLAVE\n                | FOR logic_operation LLLAVE codigo RLLAVE\n                | FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE\n       incre    : ID INCREASE\n                | ID DECREASEdecVar : decVarOne\n              | VAR ID EQUAL INTEGER\n              | VAR ID EQUAL ID\n              | VAR ID EQUAL FLOAT\n              | VAR ID EQUAL expression\n              | VAR ID EQUAL logic_operation\n              | VAR ID EQUAL comparison\n              | sliceC\n              | VAR ID EQUAL STRING\n              | ID DEQUAL STRING\n              | ID DEQUAL FLOAT\n              | ID DEQUAL expression\n              | ID DEQUAL logic_operation\n              | ID DEQUAL comparisonsliceC : VAR ID LCORCHE RCORCHE data_types\n              | ID DEQUAL funM\n              | ID DEQUAL LCORCHE RCORCHE data_types arr_content\n       funM : MAKE LPAREN LCORCHE RCORCHE data_types COMA cap RPAREN\n            | MAKE LPAREN LCORCHE RCORCHE data_types COMA cap COMA cap RPAREN\n            \n       cap : INTEGER \n           | ID\n           | expressionfunciones : APPEND LPAREN ID COMA values RPAREN\n                 | APPEND LPAREN ID COMA ID RPAREN\n                 | LEN LPAREN ID RPAREN\n                 | COPY LPAREN ID COMA ID RPAREN\n                 | DELETE LPAREN ID COMA ID RPARENdecVarOne : ID DEQUAL ID\n                 | ID DEQUAL INTEGERSenIF : IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE\n             | IF LPAREN TRUE RPAREN LLLAVE codigo RLLAVE\n             | IF LPAREN FALSE RPAREN LLLAVE codigo RLLAVESenStruct : TYPE ID STRUCT LLLAVE declaration RLLAVE\n    \n       declaration : variable data_types\n                   | declaration variable data_types\n       \n       variable    : IDcomparison : value op value\n       value      : ID\n                  | expression\n       op         : GREATER\n                  | SMALLER\n                  | GREATER_OR_EQUAL\n                  | SMALLER_OR_EQUAL\n                  | EQUAL_COMPARE\n                  | NOT_EQUALlogic_operation : logic_value logic_op logic_value\n                       | negation\n\n       logic_value     : negation\n                       | comparison\n                       | ID\n\n       negation        : NOT comparison\n                       | NOT ID\n                       \n       logic_op        : AND\n                       | ORswitch_statement : SWITCH ID LLLAVE cases RLLAVE\n\n                  cases : CASE values POINTS codigo \n                        | CASE values POINTS codigo more\n\n                  more : cases \n                       | DEFAULT POINTS codigoarray_declaration : VAR ID LCORCHE capacity RCORCHE data_types\n                         | VAR ID EQUAL LCORCHE capacity RCORCHE data_types arr_content\n\n       capacity : INTEGER \n                | ID\n                | expressionarray_var : ID LCORCHE index RCORCHE\n         \n           index : ID\n                 | INTEGER\n                 | expressionarray_assignment : array_var EQUAL somethingmap_declaration : VAR ID LCORCHE data_types RCORCHE data_typesmap_var : ID LCORCHE key RCORCHE\n           key : ID \n               | values\n               | operationsmap_assignment : array_var EQUAL somethingfunc_declaration : FUNC ID LPAREN params RPAREN data_types LLLAVE codigo RETURN retorno RLLAVE\n                        | FUNC ID LPAREN params RPAREN data_types LLLAVE RETURN return_value RLLAVE\n\n                return_value : retorno COLON\n                             | retorno\n                \n                retorno : ID \n                        | values\n                        | operations\n                        | data_structure\n                        \n                params : ID data_types \n                       | more_params\n                       \n                more_params : ID data_types COMA paramsimpresion : PRINT LPAREN expression RPARENexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : INTEGERfactor : IDfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'PRINT':([0,57,108,109,211,212,213,240,243,258,276,],[18,18,18,18,18,18,18,18,18,18,18,]),'FOR':([0,57,108,109,211,212,213,240,243,258,276,],[21,21,21,21,21,21,21,21,21,21,21,]),'VAR':([0,57,108,109,211,212,213,240,243,258,276,],[26,26,26,26,26,26,26,26,26,26,26,]),'ID':([0,19,21,26,35,36,37,39,42,43,48,52,55,56,57,63,64,65,66,67,68,69,70,71,72,74,75,76,77,78,79,80,108,109,110,111,118,119,143,144,159,166,167,168,169,170,171,172,173,174,178,180,181,185,199,211,212,213,215,228,239,240,241,243,255,258,261,263,268,276,277,284,286,],[27,54,61,73,81,82,83,85,54,54,90,54,54,54,27,113,-100,-101,-102,-103,-104,-105,117,-113,-114,120,130,134,135,136,137,113,27,27,113,150,152,160,188,191,160,-31,-32,-33,-34,-35,-36,-37,-38,-39,206,209,210,214,223,27,27,27,214,250,-94,27,188,27,-95,27,250,274,278,27,278,250,274,]),'APPEND':([0,57,108,109,211,212,213,240,243,258,276,],[30,30,30,30,30,30,30,30,30,30,30,]),'LEN':([0,57,108,109,211,212,213,240,243,258,276,],[31,31,31,31,31,31,31,31,31,31,31,]),'COPY':([0,57,108,109,211,212,213,240,243,258,276,],[32,32,32,32,32,32,32,32,32,32,32,]),'DELETE':([0,57,108,109,211,212,213,240,243,258,276,],[33,33,33,33,33,33,33,33,33,33,33,]),'IF':([0,57,108,109,211,212,213,240,243,258,276,],[34,34,34,34,34,34,34,34,34,34,34,]),'TYPE':([0,57,108,109,211,212,213,240,243,258,276,],[35,35,35,35,35,35,35,35,35,35,35,]),'SWITCH':([0,57,108,109,211,212,213,240,243,258,276,],[36,36,36,36,36,36,36,36,36,36,36,]),'FUNC':([0,57,108,109,211,212,213,240,243,258,276,],[37,37,37,37,37,37,37,37,37,37,37,]),'NOT':([0,21,48,57,70,71,72,74,108,109,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[39,39,39,39,39,-113,-114,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'INTEGER':([0,19,21,39,42,43,48,52,55,56,57,63,64,65,66,67,68,69,70,71,72,74,75,80,108,109,110,111,118,119,144,159,178,187,211,212,213,228,240,243,258,261,263,268,276,277,284,286,],[28,28,28,28,28,28,96,28,28,28,28,28,-100,-101,-102,-103,-104,-105,28,-113,-114,126,132,28,28,28,28,151,153,164,193,164,208,208,28,28,28,96,28,28,28,96,273,96,28,96,96,273,]),'LPAREN':([0,18,19,21,30,31,32,33,34,39,42,43,48,52,55,56,57,63,64,65,66,67,68,69,70,71,72,74,75,80,83,108,109,110,118,119,129,144,159,211,212,213,228,240,243,258,261,263,268,276,277,284,286,],[19,52,19,19,76,77,78,79,80,19,19,19,19,19,19,19,19,19,-100,-101,-102,-103,-104,-105,19,-113,-114,19,19,19,143,19,19,19,19,19,176,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,25,27,28,29,38,40,41,44,45,46,47,49,50,51,54,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,120,121,122,123,124,125,126,127,145,146,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,197,198,202,217,221,225,226,227,230,231,232,233,237,252,253,254,260,262,269,285,287,290,294,295,],[0,-2,-4,-5,-6,-7,-9,-10,-12,-13,-14,-16,-18,-20,-22,-24,-25,-150,-61,-107,-155,-154,-68,-153,-1,-3,-8,-11,-15,-17,-19,-21,-23,-155,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,-147,-55,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,-56,-57,-75,-115,-131,-120,-130,-77,-84,-83,-86,-87,-93,-90,-91,-92,-121,-46,-58,-45,-78,-137,-136,-79,]),'COLON':([2,3,7,8,12,13,14,15,16,20,22,25,27,28,29,38,54,60,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,120,121,122,123,124,125,126,127,145,149,150,151,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,202,221,225,226,227,230,231,232,233,260,262,278,280,281,282,283,285,287,295,],[40,41,44,45,46,47,49,50,51,-150,-61,-107,-155,-154,-68,-153,-155,110,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,-147,199,-88,-89,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,-75,-131,-120,-130,-77,-84,-83,-86,-87,-121,-46,-140,291,-141,-142,-143,-45,-78,-79,]),'RLLAVE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,25,27,28,29,38,40,41,44,45,46,47,49,50,51,54,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,112,113,114,115,116,117,120,121,122,123,124,125,126,127,145,146,147,148,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,186,197,198,202,215,217,221,225,226,227,230,231,232,233,234,235,236,237,239,247,248,249,250,252,253,254,255,256,259,260,262,264,265,269,270,271,278,279,280,281,282,283,285,287,288,289,290,291,292,294,295,],[-2,-4,-5,-6,-7,-9,-10,-12,-13,-14,-16,-18,-20,-22,-24,-25,-150,-61,-107,-155,-154,-68,-153,-1,-3,-8,-11,-15,-17,-19,-21,-23,-155,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,146,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,-147,-55,197,198,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,217,-56,-57,-75,237,-115,-131,-120,-130,-77,-84,-83,-86,-87,252,253,254,-93,-94,262,-49,-50,-155,-90,-91,-92,-95,-116,269,-121,-46,-117,-118,-58,-48,285,-140,290,-139,-141,-142,-143,-45,-78,-119,294,-137,-138,-47,-136,-79,]),'DEFAULT':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,25,27,28,29,38,40,41,44,45,46,47,49,50,51,54,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,120,121,122,123,124,125,126,127,145,146,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,197,198,202,217,221,225,226,227,230,231,232,233,237,252,253,254,256,260,262,269,285,287,290,294,295,],[-2,-4,-5,-6,-7,-9,-10,-12,-13,-14,-16,-18,-20,-22,-24,-25,-150,-61,-107,-155,-154,-68,-153,-1,-3,-8,-11,-15,-17,-19,-21,-23,-155,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,-147,-55,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,-56,-57,-75,-115,-131,-120,-130,-77,-84,-83,-86,-87,-93,-90,-91,-92,266,-121,-46,-58,-45,-78,-137,-136,-79,]),'CASE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,25,27,28,29,38,40,41,44,45,46,47,49,50,51,54,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,120,121,122,123,124,125,126,127,142,145,146,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,197,198,202,217,221,225,226,227,230,231,232,233,237,252,253,254,256,260,262,269,285,287,290,294,295,],[-2,-4,-5,-6,-7,-9,-10,-12,-13,-14,-16,-18,-20,-22,-24,-25,-150,-61,-107,-155,-154,-68,-153,-1,-3,-8,-11,-15,-17,-19,-21,-23,-155,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,187,-147,-55,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,-56,-57,-75,-115,-131,-120,-130,-77,-84,-83,-86,-87,-93,-90,-91,-92,187,-121,-46,-58,-45,-78,-137,-136,-79,]),'RETURN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,22,25,27,28,29,38,40,41,44,45,46,47,49,50,51,54,62,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,120,121,122,123,124,125,126,127,145,146,152,153,154,155,156,157,158,166,167,168,169,170,171,172,173,174,177,179,197,198,202,217,221,225,226,227,230,231,232,233,237,252,253,254,258,260,262,267,269,285,287,290,294,295,],[-2,-4,-5,-6,-7,-9,-10,-12,-13,-14,-16,-18,-20,-22,-24,-25,-150,-61,-107,-155,-154,-68,-153,-1,-3,-8,-11,-15,-17,-19,-21,-23,-155,-99,-111,-112,-148,-149,-43,-129,-51,-52,-53,-54,-44,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,-88,-70,-71,-72,-73,-74,-89,-76,-147,-55,-63,-62,-64,-65,-66,-67,-69,-31,-32,-33,-34,-35,-36,-37,-38,-39,-125,-85,-56,-57,-75,-115,-131,-120,-130,-77,-84,-83,-86,-87,-93,-90,-91,-92,268,-121,-46,277,-58,-45,-78,-137,-136,-79,]),'PLUS':([3,20,27,28,38,53,54,61,62,85,86,87,90,96,100,103,104,105,106,113,117,120,123,126,130,132,133,152,153,155,160,164,165,191,193,194,250,273,274,275,278,],[42,-150,-155,-154,-153,42,-155,-155,42,-155,-148,-149,-155,-154,42,42,-156,-151,-152,-155,-155,-155,42,-154,-155,-154,42,-155,-154,42,-155,-154,42,-155,-154,42,-155,-154,-155,42,-155,]),'MINUS':([3,20,27,28,38,53,54,61,62,85,86,87,90,96,100,103,104,105,106,113,117,120,123,126,130,132,133,152,153,155,160,164,165,191,193,194,250,273,274,275,278,],[43,-150,-155,-154,-153,43,-155,-155,43,-155,-148,-149,-155,-154,43,43,-156,-151,-152,-155,-155,-155,43,-154,-155,-154,43,-155,-154,43,-155,-154,43,-155,-154,43,-155,-154,-155,43,-155,]),'GREATER':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,64,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'SMALLER':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,65,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'GREATER_OR_EQUAL':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,66,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'SMALLER_OR_EQUAL':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,67,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'EQUAL_COMPARE':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,68,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'NOT_EQUAL':([3,20,23,27,28,38,54,61,62,85,86,87,90,96,100,104,105,106,113,117,120,123,126,152,153,155,191,193,194,250,278,],[-99,-150,69,-98,-154,-153,-155,-98,-99,-98,-148,-149,-98,-154,-99,-156,-151,-152,-98,-98,-98,-99,-154,-98,-154,-99,-98,-154,-99,-98,-98,]),'AND':([5,20,24,25,27,28,38,54,58,61,62,84,85,86,87,90,101,104,105,106,112,113,120,125,152,157,191,250,278,],[-109,-150,71,-108,-110,-154,-153,-155,-109,-110,-99,-111,-112,-148,-149,-110,-109,-156,-151,-152,-97,-98,-110,-109,-110,-109,-110,-110,-110,]),'OR':([5,20,24,25,27,28,38,54,58,61,62,84,85,86,87,90,101,104,105,106,112,113,120,125,152,157,191,250,278,],[-109,-150,72,-108,-110,-154,-153,-155,-109,-110,-99,-111,-112,-148,-149,-110,-109,-156,-151,-152,-97,-98,-110,-109,-110,-109,-110,-110,-110,]),'EQUAL':([13,73,177,],[48,118,-125,]),'RPAREN':([20,28,38,53,54,62,86,87,95,97,98,99,103,104,105,106,112,113,135,138,139,140,166,167,168,169,170,171,172,173,174,189,190,206,207,208,209,210,219,257,272,273,274,275,293,],[-150,-154,-153,104,-155,-99,-148,-149,-26,-28,-29,-30,145,-156,-151,-152,-97,-98,179,182,183,184,-31,-32,-33,-34,-35,-36,-37,-38,-39,220,-145,230,231,-27,232,233,-144,-146,287,-80,-81,-82,295,]),'LLLAVE':([20,21,25,28,38,54,58,59,62,82,84,85,86,87,104,105,106,112,113,114,115,116,117,141,166,167,168,169,170,171,172,173,174,182,183,184,204,222,242,244,245,246,],[-150,57,-107,-154,-153,-155,108,109,-99,142,-111,-112,-148,-149,-156,-151,-152,-97,-98,-106,-108,-109,-110,185,-31,-32,-33,-34,-35,-36,-37,-38,-39,211,212,213,228,243,258,-59,-60,228,]),'RCORCHE':([20,25,28,38,54,62,84,85,86,87,95,97,98,99,101,102,104,105,106,112,113,114,115,116,117,119,128,130,131,132,133,160,161,163,164,165,166,167,168,169,170,171,172,173,174,191,192,193,194,195,196,200,205,],[-150,-107,-154,-153,-155,-99,-111,-112,-148,-149,-26,-28,-29,-30,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,162,175,-126,177,-127,-128,-123,201,203,-122,-124,-31,-32,-33,-34,-35,-36,-37,-38,-39,-126,221,-27,-40,-133,-134,224,229,]),'COMA':([20,25,28,38,54,62,84,85,86,87,95,96,97,98,99,100,101,102,104,105,106,112,113,114,115,116,117,134,136,137,166,167,168,169,170,171,172,173,174,219,247,248,249,250,251,270,272,273,274,275,],[-150,-107,-154,-153,-155,-99,-111,-112,-148,-149,-26,-27,-28,-29,-30,-40,-41,-42,-156,-151,-152,-97,-98,-106,-108,-109,-110,178,180,181,-31,-32,-33,-34,-35,-36,-37,-38,-39,241,261,-49,-50,-155,263,284,286,-80,-81,-82,]),'TIMES':([20,27,28,38,54,61,85,86,87,90,96,104,105,106,113,117,120,126,130,132,152,153,160,164,191,193,250,273,274,278,],[55,-155,-154,-153,-155,-155,-155,55,55,-155,-154,-156,-151,-152,-155,-155,-155,-154,-155,-154,-155,-154,-155,-154,-155,-154,-155,-154,-155,-155,]),'DIVIDE':([20,27,28,38,54,61,85,86,87,90,96,104,105,106,113,117,120,126,130,132,152,153,160,164,191,193,250,273,274,278,],[56,-155,-154,-153,-155,-155,-155,56,56,-155,-154,-156,-151,-152,-155,-155,-155,-154,-155,-154,-155,-154,-155,-154,-155,-154,-155,-154,-155,-155,]),'DEQUAL':([27,61,],[74,111,]),'LCORCHE':([27,73,74,90,118,176,278,],[75,119,128,144,159,205,144,]),'STRING':([48,74,118,144,178,187,228,261,268,277,284,],[95,121,158,95,95,95,95,95,95,95,95,]),'FLOAT':([48,74,118,144,178,187,228,261,268,277,284,],[97,122,154,97,97,97,97,97,97,97,97,]),'TRUE':([48,80,144,178,187,228,261,268,277,284,],[98,139,98,98,98,98,98,98,98,98,]),'FALSE':([48,80,144,178,187,228,261,268,277,284,],[99,140,99,99,99,99,99,99,99,99,]),'MAKE':([74,],[129,]),'STRUCT':([81,],[141,]),'POINTS':([95,97,98,99,208,218,266,],[-26,-28,-29,-30,-27,240,276,]),'INT32':([119,162,175,188,201,203,214,216,220,224,229,238,],[166,166,166,166,166,166,-96,166,166,166,166,166,]),'INT64':([119,162,175,188,201,203,214,216,220,224,229,238,],[167,167,167,167,167,167,-96,167,167,167,167,167,]),'FLOAT32':([119,162,175,188,201,203,214,216,220,224,229,238,],[168,168,168,168,168,168,-96,168,168,168,168,168,]),'FLOAT64':([119,162,175,188,201,203,214,216,220,224,229,238,],[169,169,169,169,169,169,-96,169,169,169,169,169,]),'BYTE':([119,162,175,188,201,203,214,216,220,224,229,238,],[170,170,170,170,170,170,-96,170,170,170,170,170,]),'WINT':([119,162,175,188,201,203,214,216,220,224,229,238,],[171,171,171,171,171,171,-96,171,171,171,171,171,]),'WFLOAT':([119,162,175,188,201,203,214,216,220,224,229,238,],[172,172,172,172,172,172,-96,172,172,172,172,172,]),'WSTRING':([119,162,175,188,201,203,214,216,220,224,229,238,],[173,173,173,173,173,173,-96,173,173,173,173,173,]),'BOOL':([119,162,175,188,201,203,214,216,220,224,229,238,],[174,174,174,174,174,174,-96,174,174,174,174,174,]),'INCREASE':([223,],[244,]),'DECREASE':([223,],[245,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,57,108,109,211,212,213,240,243,258,276,],[1,107,147,148,234,235,236,256,259,267,288,]),'impresion':([0,57,108,109,211,212,213,240,243,258,276,],[2,2,2,2,2,2,2,2,2,2,2,]),'expression':([0,19,21,39,48,52,57,63,70,74,75,80,108,109,110,118,119,144,159,211,212,213,228,240,243,258,261,263,268,276,277,284,286,],[3,53,62,62,100,103,3,62,62,123,133,62,3,3,62,155,165,194,165,3,3,3,100,3,3,3,100,275,100,3,100,100,275,]),'cicloFor':([0,57,108,109,211,212,213,240,243,258,276,],[4,4,4,4,4,4,4,4,4,4,4,]),'comparison':([0,21,39,48,57,70,74,80,108,109,110,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[5,58,84,101,5,116,125,138,5,5,149,157,101,5,5,5,101,5,5,5,101,101,5,101,101,]),'logic_operation':([0,21,48,57,74,108,109,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[6,59,102,6,124,6,6,156,102,6,6,6,102,6,6,6,102,102,6,102,102,]),'decVar':([0,57,108,109,211,212,213,240,243,258,276,],[7,7,7,7,7,7,7,7,7,7,7,]),'funciones':([0,57,108,109,211,212,213,240,243,258,276,],[8,8,8,8,8,8,8,8,8,8,8,]),'SenIF':([0,57,108,109,211,212,213,240,243,258,276,],[9,9,9,9,9,9,9,9,9,9,9,]),'SenStruct':([0,57,108,109,211,212,213,240,243,258,276,],[10,10,10,10,10,10,10,10,10,10,10,]),'switch_statement':([0,57,108,109,211,212,213,240,243,258,276,],[11,11,11,11,11,11,11,11,11,11,11,]),'array_declaration':([0,57,108,109,211,212,213,240,243,258,276,],[12,12,12,12,12,12,12,12,12,12,12,]),'array_var':([0,48,57,108,109,211,212,213,240,243,258,268,276,277,],[13,88,13,13,13,13,13,13,13,13,13,88,13,88,]),'array_assignment':([0,57,108,109,211,212,213,240,243,258,276,],[14,14,14,14,14,14,14,14,14,14,14,]),'map_declaration':([0,57,108,109,211,212,213,240,243,258,276,],[15,15,15,15,15,15,15,15,15,15,15,]),'map_assignment':([0,57,108,109,211,212,213,240,243,258,276,],[16,16,16,16,16,16,16,16,16,16,16,]),'func_declaration':([0,57,108,109,211,212,213,240,243,258,276,],[17,17,17,17,17,17,17,17,17,17,17,]),'term':([0,19,21,39,42,43,48,52,57,63,70,74,75,80,108,109,110,118,119,144,159,211,212,213,228,240,243,258,261,263,268,276,277,284,286,],[20,20,20,20,86,87,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'decVarOne':([0,21,57,108,109,211,212,213,240,243,258,276,],[22,60,22,22,22,22,22,22,22,22,22,22,]),'value':([0,21,39,48,57,63,70,74,80,108,109,110,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[23,23,23,23,23,112,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'logic_value':([0,21,48,57,70,74,108,109,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[24,24,24,24,114,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'negation':([0,21,48,57,70,74,108,109,118,144,211,212,213,228,240,243,258,261,268,276,277,284,],[25,25,25,25,115,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'sliceC':([0,57,108,109,211,212,213,240,243,258,276,],[29,29,29,29,29,29,29,29,29,29,29,]),'factor':([0,19,21,39,42,43,48,52,55,56,57,63,70,74,75,80,108,109,110,118,119,144,159,211,212,213,228,240,243,258,261,263,268,276,277,284,286,],[38,38,38,38,38,38,38,38,105,106,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'op':([23,],[63,]),'logic_op':([24,],[70,]),'something':([48,],[89,]),'data_structure':([48,268,277,],[91,283,283,]),'values':([48,144,178,187,228,261,268,277,284,],[92,195,207,218,248,248,281,281,248,]),'operations':([48,144,228,261,268,277,284,],[93,196,249,249,282,282,249,]),'map_var':([48,268,277,],[94,94,94,]),'funM':([74,],[127,]),'index':([75,144,],[131,131,]),'capacity':([119,159,],[161,200,]),'data_types':([119,162,175,188,201,203,216,220,224,229,238,],[163,202,204,219,225,226,239,242,246,251,255,]),'cases':([142,256,],[186,265,]),'params':([143,241,],[189,257,]),'more_params':([143,241,],[190,190,]),'key':([144,],[192,]),'declaration':([185,],[215,]),'variable':([185,215,],[216,238,]),'incre':([199,],[222,]),'arr_content':([204,246,],[227,260,]),'items':([228,261,284,],[247,270,270,]),'more':([256,],[264,]),'more_items':([261,284,],[271,292,]),'cap':([263,286,],[272,293,]),'return_value':([268,],[279,]),'retorno':([268,277,],[280,289,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> impresion COLON','codigo',2,'p_coddigo','syntactic.py',17),
  ('codigo -> impresion','codigo',1,'p_coddigo','syntactic.py',18),
  ('codigo -> expression COLON','codigo',2,'p_coddigo','syntactic.py',20),
  ('codigo -> expression','codigo',1,'p_coddigo','syntactic.py',21),
  ('codigo -> cicloFor','codigo',1,'p_coddigo','syntactic.py',23),
  ('codigo -> comparison','codigo',1,'p_coddigo','syntactic.py',25),
  ('codigo -> logic_operation','codigo',1,'p_coddigo','syntactic.py',27),
  ('codigo -> decVar COLON','codigo',2,'p_coddigo','syntactic.py',29),
  ('codigo -> decVar','codigo',1,'p_coddigo','syntactic.py',30),
  ('codigo -> funciones','codigo',1,'p_coddigo','syntactic.py',32),
  ('codigo -> funciones COLON','codigo',2,'p_coddigo','syntactic.py',33),
  ('codigo -> SenIF','codigo',1,'p_coddigo','syntactic.py',35),
  ('codigo -> SenStruct','codigo',1,'p_coddigo','syntactic.py',37),
  ('codigo -> switch_statement','codigo',1,'p_coddigo','syntactic.py',39),
  ('codigo -> array_declaration COLON','codigo',2,'p_coddigo','syntactic.py',41),
  ('codigo -> array_declaration','codigo',1,'p_coddigo','syntactic.py',42),
  ('codigo -> array_var COLON','codigo',2,'p_coddigo','syntactic.py',43),
  ('codigo -> array_var','codigo',1,'p_coddigo','syntactic.py',44),
  ('codigo -> array_assignment COLON','codigo',2,'p_coddigo','syntactic.py',45),
  ('codigo -> array_assignment','codigo',1,'p_coddigo','syntactic.py',46),
  ('codigo -> map_declaration COLON','codigo',2,'p_coddigo','syntactic.py',48),
  ('codigo -> map_declaration','codigo',1,'p_coddigo','syntactic.py',49),
  ('codigo -> map_assignment COLON','codigo',2,'p_coddigo','syntactic.py',50),
  ('codigo -> map_assignment','codigo',1,'p_coddigo','syntactic.py',51),
  ('codigo -> func_declaration','codigo',1,'p_coddigo','syntactic.py',53),
  ('values -> STRING','values',1,'p_values','syntactic.py',56),
  ('values -> INTEGER','values',1,'p_values','syntactic.py',57),
  ('values -> FLOAT','values',1,'p_values','syntactic.py',58),
  ('values -> TRUE','values',1,'p_values','syntactic.py',59),
  ('values -> FALSE','values',1,'p_values','syntactic.py',60),
  ('data_types -> INT32','data_types',1,'p_data_types','syntactic.py',63),
  ('data_types -> INT64','data_types',1,'p_data_types','syntactic.py',64),
  ('data_types -> FLOAT32','data_types',1,'p_data_types','syntactic.py',65),
  ('data_types -> FLOAT64','data_types',1,'p_data_types','syntactic.py',66),
  ('data_types -> BYTE','data_types',1,'p_data_types','syntactic.py',67),
  ('data_types -> WINT','data_types',1,'p_data_types','syntactic.py',68),
  ('data_types -> WFLOAT','data_types',1,'p_data_types','syntactic.py',69),
  ('data_types -> WSTRING','data_types',1,'p_data_types','syntactic.py',70),
  ('data_types -> BOOL','data_types',1,'p_data_types','syntactic.py',71),
  ('operations -> expression','operations',1,'p_operations','syntactic.py',74),
  ('operations -> comparison','operations',1,'p_operations','syntactic.py',75),
  ('operations -> logic_operation','operations',1,'p_operations','syntactic.py',76),
  ('data_structure -> array_var','data_structure',1,'p_data_structure','syntactic.py',79),
  ('data_structure -> map_var','data_structure',1,'p_data_structure','syntactic.py',80),
  ('arr_content -> LLLAVE items COMA more_items RLLAVE','arr_content',5,'p_arr_content','syntactic.py',83),
  ('arr_content -> LLLAVE items RLLAVE','arr_content',3,'p_arr_content','syntactic.py',84),
  ('more_items -> items COMA more_items','more_items',3,'p_arr_content','syntactic.py',86),
  ('more_items -> items','more_items',1,'p_arr_content','syntactic.py',87),
  ('items -> values','items',1,'p_arr_content','syntactic.py',89),
  ('items -> operations','items',1,'p_arr_content','syntactic.py',90),
  ('something -> ID','something',1,'p_something','syntactic.py',93),
  ('something -> data_structure','something',1,'p_something','syntactic.py',94),
  ('something -> values','something',1,'p_something','syntactic.py',95),
  ('something -> operations','something',1,'p_something','syntactic.py',96),
  ('cicloFor -> FOR LLLAVE codigo RLLAVE','cicloFor',4,'p_for','syntactic.py',101),
  ('cicloFor -> FOR comparison LLLAVE codigo RLLAVE','cicloFor',5,'p_for','syntactic.py',102),
  ('cicloFor -> FOR logic_operation LLLAVE codigo RLLAVE','cicloFor',5,'p_for','syntactic.py',103),
  ('cicloFor -> FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE','cicloFor',9,'p_for','syntactic.py',104),
  ('incre -> ID INCREASE','incre',2,'p_for','syntactic.py',105),
  ('incre -> ID DECREASE','incre',2,'p_for','syntactic.py',106),
  ('decVar -> decVarOne','decVar',1,'p_decVar','syntactic.py',111),
  ('decVar -> VAR ID EQUAL INTEGER','decVar',4,'p_decVar','syntactic.py',112),
  ('decVar -> VAR ID EQUAL ID','decVar',4,'p_decVar','syntactic.py',113),
  ('decVar -> VAR ID EQUAL FLOAT','decVar',4,'p_decVar','syntactic.py',114),
  ('decVar -> VAR ID EQUAL expression','decVar',4,'p_decVar','syntactic.py',115),
  ('decVar -> VAR ID EQUAL logic_operation','decVar',4,'p_decVar','syntactic.py',116),
  ('decVar -> VAR ID EQUAL comparison','decVar',4,'p_decVar','syntactic.py',117),
  ('decVar -> sliceC','decVar',1,'p_decVar','syntactic.py',118),
  ('decVar -> VAR ID EQUAL STRING','decVar',4,'p_decVar','syntactic.py',119),
  ('decVar -> ID DEQUAL STRING','decVar',3,'p_decVar','syntactic.py',120),
  ('decVar -> ID DEQUAL FLOAT','decVar',3,'p_decVar','syntactic.py',121),
  ('decVar -> ID DEQUAL expression','decVar',3,'p_decVar','syntactic.py',122),
  ('decVar -> ID DEQUAL logic_operation','decVar',3,'p_decVar','syntactic.py',123),
  ('decVar -> ID DEQUAL comparison','decVar',3,'p_decVar','syntactic.py',124),
  ('sliceC -> VAR ID LCORCHE RCORCHE data_types','sliceC',5,'p_sliceC','syntactic.py',130),
  ('sliceC -> ID DEQUAL funM','sliceC',3,'p_sliceC','syntactic.py',131),
  ('sliceC -> ID DEQUAL LCORCHE RCORCHE data_types arr_content','sliceC',6,'p_sliceC','syntactic.py',132),
  ('funM -> MAKE LPAREN LCORCHE RCORCHE data_types COMA cap RPAREN','funM',8,'p_sliceC','syntactic.py',133),
  ('funM -> MAKE LPAREN LCORCHE RCORCHE data_types COMA cap COMA cap RPAREN','funM',10,'p_sliceC','syntactic.py',134),
  ('cap -> INTEGER','cap',1,'p_sliceC','syntactic.py',136),
  ('cap -> ID','cap',1,'p_sliceC','syntactic.py',137),
  ('cap -> expression','cap',1,'p_sliceC','syntactic.py',138),
  ('funciones -> APPEND LPAREN ID COMA values RPAREN','funciones',6,'p_funciones','syntactic.py',143),
  ('funciones -> APPEND LPAREN ID COMA ID RPAREN','funciones',6,'p_funciones','syntactic.py',144),
  ('funciones -> LEN LPAREN ID RPAREN','funciones',4,'p_funciones','syntactic.py',145),
  ('funciones -> COPY LPAREN ID COMA ID RPAREN','funciones',6,'p_funciones','syntactic.py',146),
  ('funciones -> DELETE LPAREN ID COMA ID RPAREN','funciones',6,'p_funciones','syntactic.py',147),
  ('decVarOne -> ID DEQUAL ID','decVarOne',3,'p_decVarOne','syntactic.py',150),
  ('decVarOne -> ID DEQUAL INTEGER','decVarOne',3,'p_decVarOne','syntactic.py',151),
  ('SenIF -> IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE','SenIF',7,'p_if','syntactic.py',158),
  ('SenIF -> IF LPAREN TRUE RPAREN LLLAVE codigo RLLAVE','SenIF',7,'p_if','syntactic.py',159),
  ('SenIF -> IF LPAREN FALSE RPAREN LLLAVE codigo RLLAVE','SenIF',7,'p_if','syntactic.py',160),
  ('SenStruct -> TYPE ID STRUCT LLLAVE declaration RLLAVE','SenStruct',6,'p_struct','syntactic.py',163),
  ('declaration -> variable data_types','declaration',2,'p_struct','syntactic.py',165),
  ('declaration -> declaration variable data_types','declaration',3,'p_struct','syntactic.py',166),
  ('variable -> ID','variable',1,'p_struct','syntactic.py',168),
  ('comparison -> value op value','comparison',3,'p_comparison','syntactic.py',173),
  ('value -> ID','value',1,'p_comparison','syntactic.py',174),
  ('value -> expression','value',1,'p_comparison','syntactic.py',175),
  ('op -> GREATER','op',1,'p_comparison','syntactic.py',176),
  ('op -> SMALLER','op',1,'p_comparison','syntactic.py',177),
  ('op -> GREATER_OR_EQUAL','op',1,'p_comparison','syntactic.py',178),
  ('op -> SMALLER_OR_EQUAL','op',1,'p_comparison','syntactic.py',179),
  ('op -> EQUAL_COMPARE','op',1,'p_comparison','syntactic.py',180),
  ('op -> NOT_EQUAL','op',1,'p_comparison','syntactic.py',181),
  ('logic_operation -> logic_value logic_op logic_value','logic_operation',3,'p_logic_operation','syntactic.py',184),
  ('logic_operation -> negation','logic_operation',1,'p_logic_operation','syntactic.py',185),
  ('logic_value -> negation','logic_value',1,'p_logic_operation','syntactic.py',187),
  ('logic_value -> comparison','logic_value',1,'p_logic_operation','syntactic.py',188),
  ('logic_value -> ID','logic_value',1,'p_logic_operation','syntactic.py',189),
  ('negation -> NOT comparison','negation',2,'p_logic_operation','syntactic.py',191),
  ('negation -> NOT ID','negation',2,'p_logic_operation','syntactic.py',192),
  ('logic_op -> AND','logic_op',1,'p_logic_operation','syntactic.py',194),
  ('logic_op -> OR','logic_op',1,'p_logic_operation','syntactic.py',195),
  ('switch_statement -> SWITCH ID LLLAVE cases RLLAVE','switch_statement',5,'p_switch','syntactic.py',198),
  ('cases -> CASE values POINTS codigo','cases',4,'p_switch','syntactic.py',200),
  ('cases -> CASE values POINTS codigo more','cases',5,'p_switch','syntactic.py',201),
  ('more -> cases','more',1,'p_switch','syntactic.py',203),
  ('more -> DEFAULT POINTS codigo','more',3,'p_switch','syntactic.py',204),
  ('array_declaration -> VAR ID LCORCHE capacity RCORCHE data_types','array_declaration',6,'p_array_declaration','syntactic.py',207),
  ('array_declaration -> VAR ID EQUAL LCORCHE capacity RCORCHE data_types arr_content','array_declaration',8,'p_array_declaration','syntactic.py',208),
  ('capacity -> INTEGER','capacity',1,'p_array_declaration','syntactic.py',210),
  ('capacity -> ID','capacity',1,'p_array_declaration','syntactic.py',211),
  ('capacity -> expression','capacity',1,'p_array_declaration','syntactic.py',212),
  ('array_var -> ID LCORCHE index RCORCHE','array_var',4,'p_array_var','syntactic.py',215),
  ('index -> ID','index',1,'p_array_var','syntactic.py',217),
  ('index -> INTEGER','index',1,'p_array_var','syntactic.py',218),
  ('index -> expression','index',1,'p_array_var','syntactic.py',219),
  ('array_assignment -> array_var EQUAL something','array_assignment',3,'p_array_assignment','syntactic.py',222),
  ('map_declaration -> VAR ID LCORCHE data_types RCORCHE data_types','map_declaration',6,'p_map_declaration','syntactic.py',225),
  ('map_var -> ID LCORCHE key RCORCHE','map_var',4,'p_map_var','syntactic.py',228),
  ('key -> ID','key',1,'p_map_var','syntactic.py',229),
  ('key -> values','key',1,'p_map_var','syntactic.py',230),
  ('key -> operations','key',1,'p_map_var','syntactic.py',231),
  ('map_assignment -> array_var EQUAL something','map_assignment',3,'p_map_assignment','syntactic.py',234),
  ('func_declaration -> FUNC ID LPAREN params RPAREN data_types LLLAVE codigo RETURN retorno RLLAVE','func_declaration',11,'p_func_declaration','syntactic.py',237),
  ('func_declaration -> FUNC ID LPAREN params RPAREN data_types LLLAVE RETURN return_value RLLAVE','func_declaration',10,'p_func_declaration','syntactic.py',238),
  ('return_value -> retorno COLON','return_value',2,'p_func_declaration','syntactic.py',240),
  ('return_value -> retorno','return_value',1,'p_func_declaration','syntactic.py',241),
  ('retorno -> ID','retorno',1,'p_func_declaration','syntactic.py',243),
  ('retorno -> values','retorno',1,'p_func_declaration','syntactic.py',244),
  ('retorno -> operations','retorno',1,'p_func_declaration','syntactic.py',245),
  ('retorno -> data_structure','retorno',1,'p_func_declaration','syntactic.py',246),
  ('params -> ID data_types','params',2,'p_func_declaration','syntactic.py',248),
  ('params -> more_params','params',1,'p_func_declaration','syntactic.py',249),
  ('more_params -> ID data_types COMA params','more_params',4,'p_func_declaration','syntactic.py',251),
  ('impresion -> PRINT LPAREN expression RPAREN','impresion',4,'p_impresion','syntactic.py',257),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','syntactic.py',262),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','syntactic.py',266),
  ('expression -> term','expression',1,'p_expression_term','syntactic.py',270),
  ('term -> term TIMES factor','term',3,'p_term_times','syntactic.py',274),
  ('term -> term DIVIDE factor','term',3,'p_term_div','syntactic.py',278),
  ('term -> factor','term',1,'p_term_factor','syntactic.py',282),
  ('factor -> INTEGER','factor',1,'p_factor_num','syntactic.py',286),
  ('factor -> ID','factor',1,'p_factor_id','syntactic.py',289),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','syntactic.py',292),
]
