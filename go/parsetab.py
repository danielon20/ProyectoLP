
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ARRAY BOOL BYTE CAP CASE COLON COMA COMMENT CONST COPY DECREASE DEQUAL DIVIDE ELSE EQUAL EQUAL_COMPARE FALSE FLOAT FLOAT32 FLOAT64 FOR FUNC GREATER GREATER_OR_EQUAL ID IF INCREASE INT32 INT64 INTEGER INTERFACE JOIN LCORCHE LEN LLLAVE LPAREN MAIN MAKE MAP MINUS MOD MULTI_COMMENT NOT NOT_EQUAL OR PACKAGE PLUS POINTER PRINT RCORCHE RLLAVE RPAREN SCAN SMALLER SMALLER_OR_EQUAL STRING STRUCT SWITCH TIMES TRUE TYPE VAR WFLOAT WINT WSTRINGcodigo : impresion\n              | expression\n              | cicloFor\n              | comparison\n              | logic_operation\n              | decVar\n              | funciones\n              | agrupaciones\n              | SenIF\n              | SenStructcicloFor : FOR LLLAVE codigo RLLAVE\n                | FOR comparison LLLAVE codigo RLLAVE\n                | FOR logic_operation LLLAVE codigo RLLAVE\n                | FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE\n       incre    : ID INCREASE\n                | ID DECREASEdecVar : decVarOne\n              | VAR ID EQUAL INTEGER\n              | VAR ID EQUAL ID\n              | VAR ID EQUAL FLOAT\n              | VAR ID EQUAL expression\n              | sliceC\n              | VAR ID EQUAL STRING\n              | ID DEQUAL STRING\n              | ID DEQUAL FLOATsliceC : VAR ID LCORCHE RCORCHE type\n              | ID DEQUAL funM\n              | ID DEQUAL LCORCHE RCORCHE type agrupaciones\n       funM : MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER RPAREN\n            | MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER COMA INTEGER RPAREN\n       type : INT32\n            | INT64\n            | FLOAT32\n            | FLOAT64\n            | BYTE\n            | WINT\n            | WFLOAT\n            | WSTRINGagrupaciones : LLLAVE INTEGER RLLAVE\n                    | LLLAVE INTEGER enteros RLLAVE\n                    | LLLAVE FLOAT RLLAVE\n                    | LLLAVE FLOAT flotantes RLLAVE\n                    | LLLAVE STRING RLLAVE\n                    | LLLAVE STRING palabras RLLAVE\n       enteros   : COMA INTEGER\n                 | COMA INTEGER enteros\n       flotantes : COMA FLOAT\n                 | COMA FLOAT flotantes\n       palabras  : COMA STRING\n                 | COMA STRING palabrasfunciones : APPEND LPAREN ID COMA INTEGER RPAREN\n                 | APPEND LPAREN ID COMA FLOAT RPAREN\n                 | APPEND LPAREN ID COMA STRING RPAREN\n                 | APPEND LPAREN ID COMA ID RPAREN\n                 | LEN LPAREN ID RPAREN\n                 | COPY LPAREN ID COMA ID RPARENdecVarOne : ID DEQUAL ID\n                 | ID DEQUAL INTEGERSenIF : IF LPAREN comparison RPAREN LLLAVE codigo RLLAVESenStruct : TYPE ID STRUCT LLLAVE declaration RLLAVE\n    \n       declaration : tipo variable\n        \n       tipo        : INT32\n                   | INT64\n                   | FLOAT32\n                   | FLOAT64\n                   | WSTRING\n                   | BOOL\n       \n       variable    : IDcomparison : value op value\n       value      : ID\n                  | expression\n       op         : GREATER\n                  | SMALLER\n                  | GREATER_OR_EQUAL\n                  | SMALLER_OR_EQUAL\n                  | EQUAL_COMPARE\n                  | NOT_EQUALlogic_operation : logic_value logic_op logic_value\n                       | negation\n\n       logic_value     : negation\n                       | comparison\n\n       negation        : NOT comparison\n                       | NOT ID\n                       \n       logic_op        : AND\n                       | ORimpresion : PRINT LPAREN expression RPARENexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : INTEGERfactor : IDfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'PRINT':([0,39,74,75,152,174,],[12,12,12,12,12,12,]),'FOR':([0,39,74,75,152,174,],[15,15,15,15,15,15,]),'VAR':([0,39,74,75,152,174,],[21,21,21,21,21,21,]),'ID':([0,13,15,21,29,31,32,33,34,37,38,39,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,74,75,76,77,92,125,127,132,152,154,155,156,157,158,159,160,174,],[22,36,43,58,64,66,36,36,36,36,36,22,88,-72,-73,-74,-75,-76,-77,88,-84,-85,94,101,102,103,88,22,22,88,94,117,147,151,162,22,173,-62,-63,-64,-65,-66,-67,22,]),'APPEND':([0,39,74,75,152,174,],[25,25,25,25,25,25,]),'LEN':([0,39,74,75,152,174,],[26,26,26,26,26,26,]),'COPY':([0,39,74,75,152,174,],[27,27,27,27,27,27,]),'LLLAVE':([0,14,15,20,23,30,36,39,40,41,44,65,66,67,68,70,71,72,74,75,87,88,89,90,91,105,128,137,138,139,140,141,142,143,144,145,152,161,174,175,176,],[16,-89,39,-79,-93,-92,-94,16,74,75,-71,-82,-83,-87,-88,-95,-90,-91,16,16,-69,-70,-78,-80,-81,129,152,-31,-32,-33,-34,-35,-36,-37,-38,16,16,174,16,-15,-16,]),'IF':([0,39,74,75,152,174,],[28,28,28,28,28,28,]),'TYPE':([0,39,74,75,152,174,],[29,29,29,29,29,29,]),'NOT':([0,15,39,55,56,57,74,75,152,174,],[31,31,31,31,-84,-85,31,31,31,31,]),'INTEGER':([0,13,15,16,31,32,33,34,37,38,39,48,49,50,51,52,53,54,55,56,57,59,63,74,75,76,77,80,92,125,152,174,180,183,],[23,23,23,45,23,23,23,23,23,23,23,23,-72,-73,-74,-75,-76,-77,23,-84,-85,97,23,23,23,23,97,112,118,148,23,23,182,185,]),'LPAREN':([0,12,13,15,25,26,27,28,31,32,33,34,37,38,39,48,49,50,51,52,53,54,55,56,57,63,74,75,76,92,100,152,174,],[13,34,13,13,60,61,62,63,13,13,13,13,13,13,13,13,-72,-73,-74,-75,-76,-77,13,-84,-85,13,13,13,13,13,124,13,13,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,14,17,20,22,23,24,30,36,44,65,66,67,68,70,71,72,78,81,84,87,88,89,90,91,94,95,96,97,98,106,107,111,113,115,117,118,119,120,121,126,130,131,136,137,138,139,140,141,142,143,144,163,165,166,167,168,169,171,178,181,184,186,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-89,-17,-79,-94,-93,-22,-92,-94,-71,-82,-83,-87,-88,-95,-90,-91,-39,-41,-43,-69,-70,-78,-80,-81,-57,-24,-25,-58,-27,-86,-11,-40,-42,-44,-19,-18,-20,-21,-23,-55,-12,-13,-26,-31,-32,-33,-34,-35,-36,-37,-38,-28,-54,-51,-52,-53,-56,-60,-59,-14,-29,-30,]),'RLLAVE':([2,3,4,5,6,7,8,9,10,11,14,17,20,22,23,24,30,36,44,45,46,47,65,66,67,68,70,71,72,73,78,79,81,82,84,85,87,88,89,90,91,94,95,96,97,98,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,126,130,131,133,134,135,136,137,138,139,140,141,142,143,144,153,163,165,166,167,168,169,170,171,172,173,178,179,181,184,186,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-89,-17,-79,-94,-93,-22,-92,-94,-71,78,81,84,-82,-83,-87,-88,-95,-90,-91,107,-39,111,-41,113,-43,115,-69,-70,-78,-80,-81,-57,-24,-25,-58,-27,-86,-11,130,131,-40,-45,-42,-47,-44,-49,-19,-18,-20,-21,-23,-55,-12,-13,-46,-48,-50,-26,-31,-32,-33,-34,-35,-36,-37,-38,171,-28,-54,-51,-52,-53,-56,178,-60,-61,-68,-59,181,-14,-29,-30,]),'PLUS':([3,14,22,23,30,35,36,43,44,66,67,68,69,70,71,72,88,117,118,120,],[32,-89,-94,-93,-92,32,-94,-94,32,-94,-87,-88,32,-95,-90,-91,-94,-94,-93,32,]),'MINUS':([3,14,22,23,30,35,36,43,44,66,67,68,69,70,71,72,88,117,118,120,],[33,-89,-94,-93,-92,33,-94,-94,33,-94,-87,-88,33,-95,-90,-91,-94,-94,-93,33,]),'GREATER':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,49,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'SMALLER':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,50,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'GREATER_OR_EQUAL':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,51,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'SMALLER_OR_EQUAL':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,52,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'EQUAL_COMPARE':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,53,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'NOT_EQUAL':([3,14,18,22,23,30,36,43,44,66,67,68,70,71,72,88,],[-71,-89,54,-70,-93,-92,-94,-70,-71,-70,-87,-88,-95,-90,-91,-70,]),'AND':([5,14,19,20,23,30,36,40,44,65,66,67,68,70,71,72,87,88,],[-81,-89,56,-80,-93,-92,-94,-81,-71,-82,-83,-87,-88,-95,-90,-91,-69,-70,]),'OR':([5,14,19,20,23,30,36,40,44,65,66,67,68,70,71,72,87,88,],[-81,-89,57,-80,-93,-92,-94,-81,-71,-82,-83,-87,-88,-95,-90,-91,-69,-70,]),'RPAREN':([14,23,30,35,36,44,67,68,69,70,71,72,87,88,102,104,147,148,149,150,151,182,185,],[-89,-93,-92,70,-94,-71,-87,-88,106,-95,-90,-91,-69,-70,126,128,165,166,167,168,169,184,186,]),'COLON':([14,23,30,36,42,44,67,68,70,71,72,87,88,94,97,110,],[-89,-93,-92,-94,76,-71,-87,-88,-95,-90,-91,-69,-70,-57,-58,132,]),'TIMES':([14,22,23,30,36,43,66,67,68,70,71,72,88,117,118,],[37,-94,-93,-92,-94,-94,-94,37,37,-95,-90,-91,-94,-94,-93,]),'DIVIDE':([14,22,23,30,36,43,66,67,68,70,71,72,88,117,118,],[38,-94,-93,-92,-94,-94,-94,38,38,-95,-90,-91,-94,-94,-93,]),'FLOAT':([16,59,83,92,125,],[46,96,114,119,149,]),'STRING':([16,59,86,92,125,],[47,95,116,121,150,]),'DEQUAL':([22,43,],[59,77,]),'COMA':([45,46,47,101,103,112,114,116,137,138,139,140,141,142,143,144,177,182,],[80,83,86,125,127,80,83,86,-31,-32,-33,-34,-35,-36,-37,-38,180,183,]),'EQUAL':([58,],[92,]),'LCORCHE':([58,59,124,],[93,99,146,]),'MAKE':([59,],[100,]),'STRUCT':([64,],[105,]),'RCORCHE':([93,99,146,],[122,123,164,]),'INT32':([122,123,129,164,],[137,137,155,137,]),'INT64':([122,123,129,164,],[138,138,156,138,]),'FLOAT32':([122,123,129,164,],[139,139,157,139,]),'FLOAT64':([122,123,129,164,],[140,140,158,140,]),'BYTE':([122,123,164,],[141,141,141,]),'WINT':([122,123,164,],[142,142,142,]),'WFLOAT':([122,123,164,],[143,143,143,]),'WSTRING':([122,123,129,164,],[144,144,159,144,]),'BOOL':([129,],[160,]),'INCREASE':([162,],[175,]),'DECREASE':([162,],[176,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,39,74,75,152,174,],[1,73,108,109,170,179,]),'impresion':([0,39,74,75,152,174,],[2,2,2,2,2,2,]),'expression':([0,13,15,31,34,39,48,55,63,74,75,76,92,152,174,],[3,35,44,44,69,3,44,44,44,3,3,44,120,3,3,]),'cicloFor':([0,39,74,75,152,174,],[4,4,4,4,4,4,]),'comparison':([0,15,31,39,55,63,74,75,76,152,174,],[5,40,65,5,91,104,5,5,110,5,5,]),'logic_operation':([0,15,39,74,75,152,174,],[6,41,6,6,6,6,6,]),'decVar':([0,39,74,75,152,174,],[7,7,7,7,7,7,]),'funciones':([0,39,74,75,152,174,],[8,8,8,8,8,8,]),'agrupaciones':([0,39,74,75,145,152,174,],[9,9,9,9,163,9,9,]),'SenIF':([0,39,74,75,152,174,],[10,10,10,10,10,10,]),'SenStruct':([0,39,74,75,152,174,],[11,11,11,11,11,11,]),'term':([0,13,15,31,32,33,34,39,48,55,63,74,75,76,92,152,174,],[14,14,14,14,67,68,14,14,14,14,14,14,14,14,14,14,14,]),'decVarOne':([0,15,39,74,75,152,174,],[17,42,17,17,17,17,17,]),'value':([0,15,31,39,48,55,63,74,75,76,152,174,],[18,18,18,18,87,18,18,18,18,18,18,18,]),'logic_value':([0,15,39,55,74,75,152,174,],[19,19,19,89,19,19,19,19,]),'negation':([0,15,39,55,74,75,152,174,],[20,20,20,90,20,20,20,20,]),'sliceC':([0,39,74,75,152,174,],[24,24,24,24,24,24,]),'factor':([0,13,15,31,32,33,34,37,38,39,48,55,63,74,75,76,92,152,174,],[30,30,30,30,30,30,30,71,72,30,30,30,30,30,30,30,30,30,30,]),'op':([18,],[48,]),'logic_op':([19,],[55,]),'enteros':([45,112,],[79,133,]),'flotantes':([46,114,],[82,134,]),'palabras':([47,116,],[85,135,]),'funM':([59,],[98,]),'type':([122,123,164,],[136,145,177,]),'declaration':([129,],[153,]),'tipo':([129,],[154,]),'incre':([132,],[161,]),'variable':([154,],[172,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> impresion','codigo',1,'p_coddigo','syntactic.py',17),
  ('codigo -> expression','codigo',1,'p_coddigo','syntactic.py',18),
  ('codigo -> cicloFor','codigo',1,'p_coddigo','syntactic.py',19),
  ('codigo -> comparison','codigo',1,'p_coddigo','syntactic.py',20),
  ('codigo -> logic_operation','codigo',1,'p_coddigo','syntactic.py',21),
  ('codigo -> decVar','codigo',1,'p_coddigo','syntactic.py',22),
  ('codigo -> funciones','codigo',1,'p_coddigo','syntactic.py',23),
  ('codigo -> agrupaciones','codigo',1,'p_coddigo','syntactic.py',24),
  ('codigo -> SenIF','codigo',1,'p_coddigo','syntactic.py',25),
  ('codigo -> SenStruct','codigo',1,'p_coddigo','syntactic.py',26),
  ('cicloFor -> FOR LLLAVE codigo RLLAVE','cicloFor',4,'p_for','syntactic.py',31),
  ('cicloFor -> FOR comparison LLLAVE codigo RLLAVE','cicloFor',5,'p_for','syntactic.py',32),
  ('cicloFor -> FOR logic_operation LLLAVE codigo RLLAVE','cicloFor',5,'p_for','syntactic.py',33),
  ('cicloFor -> FOR decVarOne COLON comparison COLON incre LLLAVE codigo RLLAVE','cicloFor',9,'p_for','syntactic.py',34),
  ('incre -> ID INCREASE','incre',2,'p_for','syntactic.py',35),
  ('incre -> ID DECREASE','incre',2,'p_for','syntactic.py',36),
  ('decVar -> decVarOne','decVar',1,'p_decVar','syntactic.py',41),
  ('decVar -> VAR ID EQUAL INTEGER','decVar',4,'p_decVar','syntactic.py',42),
  ('decVar -> VAR ID EQUAL ID','decVar',4,'p_decVar','syntactic.py',43),
  ('decVar -> VAR ID EQUAL FLOAT','decVar',4,'p_decVar','syntactic.py',44),
  ('decVar -> VAR ID EQUAL expression','decVar',4,'p_decVar','syntactic.py',45),
  ('decVar -> sliceC','decVar',1,'p_decVar','syntactic.py',46),
  ('decVar -> VAR ID EQUAL STRING','decVar',4,'p_decVar','syntactic.py',47),
  ('decVar -> ID DEQUAL STRING','decVar',3,'p_decVar','syntactic.py',48),
  ('decVar -> ID DEQUAL FLOAT','decVar',3,'p_decVar','syntactic.py',49),
  ('sliceC -> VAR ID LCORCHE RCORCHE type','sliceC',5,'p_sliceC','syntactic.py',55),
  ('sliceC -> ID DEQUAL funM','sliceC',3,'p_sliceC','syntactic.py',56),
  ('sliceC -> ID DEQUAL LCORCHE RCORCHE type agrupaciones','sliceC',6,'p_sliceC','syntactic.py',57),
  ('funM -> MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER RPAREN','funM',8,'p_sliceC','syntactic.py',58),
  ('funM -> MAKE LPAREN LCORCHE RCORCHE type COMA INTEGER COMA INTEGER RPAREN','funM',10,'p_sliceC','syntactic.py',59),
  ('type -> INT32','type',1,'p_sliceC','syntactic.py',60),
  ('type -> INT64','type',1,'p_sliceC','syntactic.py',61),
  ('type -> FLOAT32','type',1,'p_sliceC','syntactic.py',62),
  ('type -> FLOAT64','type',1,'p_sliceC','syntactic.py',63),
  ('type -> BYTE','type',1,'p_sliceC','syntactic.py',64),
  ('type -> WINT','type',1,'p_sliceC','syntactic.py',65),
  ('type -> WFLOAT','type',1,'p_sliceC','syntactic.py',66),
  ('type -> WSTRING','type',1,'p_sliceC','syntactic.py',67),
  ('agrupaciones -> LLLAVE INTEGER RLLAVE','agrupaciones',3,'p_agrupaciones','syntactic.py',74),
  ('agrupaciones -> LLLAVE INTEGER enteros RLLAVE','agrupaciones',4,'p_agrupaciones','syntactic.py',75),
  ('agrupaciones -> LLLAVE FLOAT RLLAVE','agrupaciones',3,'p_agrupaciones','syntactic.py',76),
  ('agrupaciones -> LLLAVE FLOAT flotantes RLLAVE','agrupaciones',4,'p_agrupaciones','syntactic.py',77),
  ('agrupaciones -> LLLAVE STRING RLLAVE','agrupaciones',3,'p_agrupaciones','syntactic.py',78),
  ('agrupaciones -> LLLAVE STRING palabras RLLAVE','agrupaciones',4,'p_agrupaciones','syntactic.py',79),
  ('enteros -> COMA INTEGER','enteros',2,'p_agrupaciones','syntactic.py',80),
  ('enteros -> COMA INTEGER enteros','enteros',3,'p_agrupaciones','syntactic.py',81),
  ('flotantes -> COMA FLOAT','flotantes',2,'p_agrupaciones','syntactic.py',82),
  ('flotantes -> COMA FLOAT flotantes','flotantes',3,'p_agrupaciones','syntactic.py',83),
  ('palabras -> COMA STRING','palabras',2,'p_agrupaciones','syntactic.py',84),
  ('palabras -> COMA STRING palabras','palabras',3,'p_agrupaciones','syntactic.py',85),
  ('funciones -> APPEND LPAREN ID COMA INTEGER RPAREN','funciones',6,'p_funciones','syntactic.py',91),
  ('funciones -> APPEND LPAREN ID COMA FLOAT RPAREN','funciones',6,'p_funciones','syntactic.py',92),
  ('funciones -> APPEND LPAREN ID COMA STRING RPAREN','funciones',6,'p_funciones','syntactic.py',93),
  ('funciones -> APPEND LPAREN ID COMA ID RPAREN','funciones',6,'p_funciones','syntactic.py',94),
  ('funciones -> LEN LPAREN ID RPAREN','funciones',4,'p_funciones','syntactic.py',95),
  ('funciones -> COPY LPAREN ID COMA ID RPAREN','funciones',6,'p_funciones','syntactic.py',96),
  ('decVarOne -> ID DEQUAL ID','decVarOne',3,'p_decVarOne','syntactic.py',99),
  ('decVarOne -> ID DEQUAL INTEGER','decVarOne',3,'p_decVarOne','syntactic.py',100),
  ('SenIF -> IF LPAREN comparison RPAREN LLLAVE codigo RLLAVE','SenIF',7,'p_if','syntactic.py',107),
  ('SenStruct -> TYPE ID STRUCT LLLAVE declaration RLLAVE','SenStruct',6,'p_struct','syntactic.py',110),
  ('declaration -> tipo variable','declaration',2,'p_struct','syntactic.py',112),
  ('tipo -> INT32','tipo',1,'p_struct','syntactic.py',114),
  ('tipo -> INT64','tipo',1,'p_struct','syntactic.py',115),
  ('tipo -> FLOAT32','tipo',1,'p_struct','syntactic.py',116),
  ('tipo -> FLOAT64','tipo',1,'p_struct','syntactic.py',117),
  ('tipo -> WSTRING','tipo',1,'p_struct','syntactic.py',118),
  ('tipo -> BOOL','tipo',1,'p_struct','syntactic.py',119),
  ('variable -> ID','variable',1,'p_struct','syntactic.py',121),
  ('comparison -> value op value','comparison',3,'p_comparison','syntactic.py',126),
  ('value -> ID','value',1,'p_comparison','syntactic.py',127),
  ('value -> expression','value',1,'p_comparison','syntactic.py',128),
  ('op -> GREATER','op',1,'p_comparison','syntactic.py',129),
  ('op -> SMALLER','op',1,'p_comparison','syntactic.py',130),
  ('op -> GREATER_OR_EQUAL','op',1,'p_comparison','syntactic.py',131),
  ('op -> SMALLER_OR_EQUAL','op',1,'p_comparison','syntactic.py',132),
  ('op -> EQUAL_COMPARE','op',1,'p_comparison','syntactic.py',133),
  ('op -> NOT_EQUAL','op',1,'p_comparison','syntactic.py',134),
  ('logic_operation -> logic_value logic_op logic_value','logic_operation',3,'p_logic_operation','syntactic.py',137),
  ('logic_operation -> negation','logic_operation',1,'p_logic_operation','syntactic.py',138),
  ('logic_value -> negation','logic_value',1,'p_logic_operation','syntactic.py',140),
  ('logic_value -> comparison','logic_value',1,'p_logic_operation','syntactic.py',141),
  ('negation -> NOT comparison','negation',2,'p_logic_operation','syntactic.py',143),
  ('negation -> NOT ID','negation',2,'p_logic_operation','syntactic.py',144),
  ('logic_op -> AND','logic_op',1,'p_logic_operation','syntactic.py',146),
  ('logic_op -> OR','logic_op',1,'p_logic_operation','syntactic.py',147),
  ('impresion -> PRINT LPAREN expression RPAREN','impresion',4,'p_impresion','syntactic.py',151),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','syntactic.py',156),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','syntactic.py',160),
  ('expression -> term','expression',1,'p_expression_term','syntactic.py',164),
  ('term -> term TIMES factor','term',3,'p_term_times','syntactic.py',168),
  ('term -> term DIVIDE factor','term',3,'p_term_div','syntactic.py',172),
  ('term -> factor','term',1,'p_term_factor','syntactic.py',176),
  ('factor -> INTEGER','factor',1,'p_factor_num','syntactic.py',180),
  ('factor -> ID','factor',1,'p_factor_id','syntactic.py',183),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','syntactic.py',186),
]
