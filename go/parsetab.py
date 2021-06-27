
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ARRAY BOOL BYTE CAP CASE COLON COMA COMMENT CONST COPY DECREASE DEQUAL DIVIDE ELSE EQUAL EQUAL_COMPARE FALSE FLOAT FLOAT32 FLOAT64 FOR FUNC GREATER GREATER_OR_EQUAL ID IF INCREASE INT32 INT64 INTEGER INTERFACE JOIN LCORCHE LEN LLLAVE LPAREN MAIN MAKE MAP MINUS MOD MULTI_COMMENT NOT NOT_EQUAL OR PACKAGE PLUS POINTER PRINT RCORCHE RLLAVE RPAREN SCAN SMALLER SMALLER_OR_EQUAL STRING STRUCT SWITCH TIMES TRUE TYPE VARcodigo : impresion\n              | expression\n              | cicloFor cicloFor : FOR LLLAVE codigo RLLAVEimpresion : PRINT LPAREN expression RPARENexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : INTEGERfactor : IDfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'PRINT':([0,18,],[5,5,]),'FOR':([0,18,],[8,8,]),'INTEGER':([0,6,12,13,14,16,17,18,],[10,10,10,10,10,10,10,10,]),'ID':([0,6,12,13,14,16,17,18,],[11,11,11,11,11,11,11,11,]),'LPAREN':([0,5,6,12,13,14,16,17,18,],[6,14,6,6,6,6,6,6,6,]),'$end':([1,2,3,4,7,9,10,11,19,20,22,23,24,26,27,],[0,-1,-2,-3,-8,-11,-12,-13,-6,-7,-14,-9,-10,-5,-4,]),'RLLAVE':([2,3,4,7,9,10,11,19,20,22,23,24,25,26,27,],[-1,-2,-3,-8,-11,-12,-13,-6,-7,-14,-9,-10,27,-5,-4,]),'PLUS':([3,7,9,10,11,15,19,20,21,22,23,24,],[12,-8,-11,-12,-13,12,-6,-7,12,-14,-9,-10,]),'MINUS':([3,7,9,10,11,15,19,20,21,22,23,24,],[13,-8,-11,-12,-13,13,-6,-7,13,-14,-9,-10,]),'RPAREN':([7,9,10,11,15,19,20,21,22,23,24,],[-8,-11,-12,-13,22,-6,-7,26,-14,-9,-10,]),'TIMES':([7,9,10,11,19,20,22,23,24,],[16,-11,-12,-13,16,16,-14,-9,-10,]),'DIVIDE':([7,9,10,11,19,20,22,23,24,],[17,-11,-12,-13,17,17,-14,-9,-10,]),'LLLAVE':([8,],[18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,18,],[1,25,]),'impresion':([0,18,],[2,2,]),'expression':([0,6,14,18,],[3,15,21,3,]),'cicloFor':([0,18,],[4,4,]),'term':([0,6,12,13,14,18,],[7,7,19,20,7,7,]),'factor':([0,6,12,13,14,16,17,18,],[9,9,9,9,9,23,24,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> impresion','codigo',1,'p_coddigo','syntactic.py',16),
  ('codigo -> expression','codigo',1,'p_coddigo','syntactic.py',17),
  ('codigo -> cicloFor','codigo',1,'p_coddigo','syntactic.py',18),
  ('cicloFor -> FOR LLLAVE codigo RLLAVE','cicloFor',4,'p_for','syntactic.py',23),
  ('impresion -> PRINT LPAREN expression RPAREN','impresion',4,'p_impresion','syntactic.py',43),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','syntactic.py',48),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','syntactic.py',52),
  ('expression -> term','expression',1,'p_expression_term','syntactic.py',56),
  ('term -> term TIMES factor','term',3,'p_term_times','syntactic.py',60),
  ('term -> term DIVIDE factor','term',3,'p_term_div','syntactic.py',64),
  ('term -> factor','term',1,'p_term_factor','syntactic.py',68),
  ('factor -> INTEGER','factor',1,'p_factor_num','syntactic.py',72),
  ('factor -> ID','factor',1,'p_factor_id','syntactic.py',75),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','syntactic.py',78),
]
