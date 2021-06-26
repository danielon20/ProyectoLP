
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ARRAY BOOL BYTE CAP CASE COLON COMA COMMENT CONST COPY DECREASE DEQUAL DIVIDE ELSE EQUAL EQUAL_COMPARE FALSE FLOAT FLOAT32 FLOAT64 FOR FUNC GREATER GREATER_OR_EQUAL ID IF INCREASE INT INTEGER INTERFACE JOIN LCORCHE LEN LLLAVE LPAREN MAIN MAKE MAP MINUS MOD MULTI_COMMENT NOT NOT_EQUAL OR PACKAGE PLUS POINTER PRINT RCORCHE RLLAVE RPAREN SCAN SMALLER SMALLER_OR_EQUAL STRING STRUCT SWITCH TIMES TRUE TYPE VARcodigo : impresion\n              | expressionimpresion : PRINT LPAREN expression RPARENexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : INTEGERfactor : IDfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'PRINT':([0,],[4,]),'INTEGER':([0,5,10,11,12,14,15,],[8,8,8,8,8,8,8,]),'ID':([0,5,10,11,12,14,15,],[9,9,9,9,9,9,9,]),'LPAREN':([0,4,5,10,11,12,14,15,],[5,12,5,5,5,5,5,5,]),'$end':([1,2,3,6,7,8,9,16,17,19,20,21,22,],[0,-1,-2,-6,-9,-10,-11,-4,-5,-12,-7,-8,-3,]),'PLUS':([3,6,7,8,9,13,16,17,18,19,20,21,],[10,-6,-9,-10,-11,10,-4,-5,10,-12,-7,-8,]),'MINUS':([3,6,7,8,9,13,16,17,18,19,20,21,],[11,-6,-9,-10,-11,11,-4,-5,11,-12,-7,-8,]),'RPAREN':([6,7,8,9,13,16,17,18,19,20,21,],[-6,-9,-10,-11,19,-4,-5,22,-12,-7,-8,]),'TIMES':([6,7,8,9,16,17,19,20,21,],[14,-9,-10,-11,14,14,-12,-7,-8,]),'DIVIDE':([6,7,8,9,16,17,19,20,21,],[15,-9,-10,-11,15,15,-12,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,],[1,]),'impresion':([0,],[2,]),'expression':([0,5,12,],[3,13,18,]),'term':([0,5,10,11,12,],[6,6,16,17,6,]),'factor':([0,5,10,11,12,14,15,],[7,7,7,7,7,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> impresion','codigo',1,'p_coddigo','test.py',16),
  ('codigo -> expression','codigo',1,'p_coddigo','test.py',17),
  ('impresion -> PRINT LPAREN expression RPAREN','impresion',4,'p_impresion','test.py',20),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','test.py',23),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','test.py',27),
  ('expression -> term','expression',1,'p_expression_term','test.py',31),
  ('term -> term TIMES factor','term',3,'p_term_times','test.py',35),
  ('term -> term DIVIDE factor','term',3,'p_term_div','test.py',39),
  ('term -> factor','term',1,'p_term_factor','test.py',43),
  ('factor -> INTEGER','factor',1,'p_factor_num','test.py',47),
  ('factor -> ID','factor',1,'p_factor_id','test.py',50),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','test.py',53),
]
