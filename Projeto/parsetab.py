
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT CPAR DOT ELSE EQUAL ID IF INDENTATION NEWLINE OPAR TAG VAR VARNAME VARVALUEpugHTML : pugHTML linhas\n                | linhas : linhas linha\n           | linhalinha : INDENTATION line NEWLINE\n            | line NEWLINE\n            | NEWLINEline : tagline\n            | tagdotline\n            | trashline\n            | cardinalline\n            | varline\n            | ifline\n            | elselineelseline : ELSE ifline : IF VARNAME EQUAL VARVALUE\n                | IF VARNAMEtagdotline : TAG OPAR VARNAME EQUAL VARVALUE CPAR DOT\n                | TAG EQUAL VARVALUE DOT\n                | TAG COMMENT DOT\n                | TAG DOTtagline : TAG OPAR VARNAME EQUAL VARVALUE CPAR\n                | TAG EQUAL VARVALUE\n                | TAG COMMENT\n                | TAGtrashline : COMMENTcardinalline : ID VARVALUE DOT VARVALUE\n                    | ID VARVALUEvarline : VAR VARNAME EQUAL VARVALUE'
    
_lr_action_items = {'INDENTATION':([0,1,2,3,6,20,22,30,],[-2,4,4,-4,-7,-3,-6,-5,]),'NEWLINE':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,19,20,21,22,25,26,27,29,30,32,33,38,39,40,41,43,44,],[-2,6,6,-4,22,-7,-8,-9,-10,-11,-12,-13,-14,-25,-26,-15,-3,30,-6,-24,-21,-28,-17,-5,-23,-20,-19,-27,-29,-16,-22,-18,]),'TAG':([0,1,2,3,4,6,20,22,30,],[-2,14,14,-4,14,-7,-3,-6,-5,]),'COMMENT':([0,1,2,3,4,6,14,20,22,30,],[-2,15,15,-4,15,-7,25,-3,-6,-5,]),'ID':([0,1,2,3,4,6,20,22,30,],[-2,16,16,-4,16,-7,-3,-6,-5,]),'VAR':([0,1,2,3,4,6,20,22,30,],[-2,17,17,-4,17,-7,-3,-6,-5,]),'IF':([0,1,2,3,4,6,20,22,30,],[-2,18,18,-4,18,-7,-3,-6,-5,]),'ELSE':([0,1,2,3,4,6,20,22,30,],[-2,19,19,-4,19,-7,-3,-6,-5,]),'$end':([0,1,2,3,6,20,22,30,],[-2,0,-1,-4,-7,-3,-6,-5,]),'OPAR':([14,],[23,]),'EQUAL':([14,28,29,31,],[24,35,36,37,]),'DOT':([14,25,27,32,43,],[26,33,34,38,44,]),'VARVALUE':([16,24,34,35,36,37,],[27,32,39,40,41,42,]),'VARNAME':([17,18,23,],[28,29,31,]),'CPAR':([42,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'pugHTML':([0,],[1,]),'linhas':([1,],[2,]),'linha':([1,2,],[3,20,]),'line':([1,2,4,],[5,5,21,]),'tagline':([1,2,4,],[7,7,7,]),'tagdotline':([1,2,4,],[8,8,8,]),'trashline':([1,2,4,],[9,9,9,]),'cardinalline':([1,2,4,],[10,10,10,]),'varline':([1,2,4,],[11,11,11,]),'ifline':([1,2,4,],[12,12,12,]),'elseline':([1,2,4,],[13,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pugHTML","S'",1,None,None,None),
  ('pugHTML -> pugHTML linhas','pugHTML',2,'p_pugHTML','newParser.py',93),
  ('pugHTML -> <empty>','pugHTML',0,'p_pugHTML','newParser.py',94),
  ('linhas -> linhas linha','linhas',2,'p_linhas','newParser.py',102),
  ('linhas -> linha','linhas',1,'p_linhas','newParser.py',103),
  ('linha -> INDENTATION line NEWLINE','linha',3,'p_linha','newParser.py',112),
  ('linha -> line NEWLINE','linha',2,'p_linha','newParser.py',113),
  ('linha -> NEWLINE','linha',1,'p_linha','newParser.py',114),
  ('line -> tagline','line',1,'p_line','newParser.py',126),
  ('line -> tagdotline','line',1,'p_line','newParser.py',127),
  ('line -> trashline','line',1,'p_line','newParser.py',128),
  ('line -> cardinalline','line',1,'p_line','newParser.py',129),
  ('line -> varline','line',1,'p_line','newParser.py',130),
  ('line -> ifline','line',1,'p_line','newParser.py',131),
  ('line -> elseline','line',1,'p_line','newParser.py',132),
  ('elseline -> ELSE','elseline',1,'p_elseline','newParser.py',137),
  ('ifline -> IF VARNAME EQUAL VARVALUE','ifline',4,'p_ifline','newParser.py',143),
  ('ifline -> IF VARNAME','ifline',2,'p_ifline','newParser.py',144),
  ('tagdotline -> TAG OPAR VARNAME EQUAL VARVALUE CPAR DOT','tagdotline',7,'p_tagdotline','newParser.py',152),
  ('tagdotline -> TAG EQUAL VARVALUE DOT','tagdotline',4,'p_tagdotline','newParser.py',153),
  ('tagdotline -> TAG COMMENT DOT','tagdotline',3,'p_tagdotline','newParser.py',154),
  ('tagdotline -> TAG DOT','tagdotline',2,'p_tagdotline','newParser.py',155),
  ('tagline -> TAG OPAR VARNAME EQUAL VARVALUE CPAR','tagline',6,'p_tagline','newParser.py',167),
  ('tagline -> TAG EQUAL VARVALUE','tagline',3,'p_tagline','newParser.py',168),
  ('tagline -> TAG COMMENT','tagline',2,'p_tagline','newParser.py',169),
  ('tagline -> TAG','tagline',1,'p_tagline','newParser.py',170),
  ('trashline -> COMMENT','trashline',1,'p_trashline','newParser.py',182),
  ('cardinalline -> ID VARVALUE DOT VARVALUE','cardinalline',4,'p_cardinalline','newParser.py',187),
  ('cardinalline -> ID VARVALUE','cardinalline',2,'p_cardinalline','newParser.py',188),
  ('varline -> VAR VARNAME EQUAL VARVALUE','varline',4,'p_varline','newParser.py',196),
]
