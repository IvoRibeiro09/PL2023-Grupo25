from ply import lex

from Defs_por_estado.ID_DEF import *
from Defs_por_estado.INITIAL_DEF import *
from Defs_por_estado.PONTO_DEF import *
from Defs_por_estado.TAG_DEF import *
from Defs_por_estado.TEXT_DEF import *
from Defs_por_estado.VARIAVEL_DEF import *
from Defs_por_estado.OPENPAR_def import *
from Defs_por_estado.IFSTATE_DEF import *
from Defs_por_estado.COMENTSTATE_DEF import *

states = (
    ('openPar', 'exclusive'),
    ('tag', 'exclusive'),
    ('text', 'exclusive'),
    ('id', 'exclusive'),
    ('ponto', 'exclusive'),
    ('variavel', 'exclusive'),
    ('ifstate', 'exclusive'),
    ('comentstate', 'exclusive')
)

tokens = [
    'NEWLINE',
    'OPAR',
    'CPAR',
    'VAR',
    'VARNAME',
    'VARVALUE',
    'ID',
    'INDENTATION',
    'IF',
    'ELSE',
    'TAG',
    'DOT',
    'COMMENT',
    'EQUAL',
    'WRCOMT',
    'RDCOMT'
]

def t_ANY_error(t):
    print("---------------------->Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
lexer.ident_linhaAntes = 0
lexer.ident_linhaAtual = 0
