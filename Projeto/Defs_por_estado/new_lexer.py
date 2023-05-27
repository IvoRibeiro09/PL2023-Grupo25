from ply import lex

from Defs_por_estado.ID_DEF import *
from Defs_por_estado.INITIAL_DEF import *
from Defs_por_estado.PONTO_DEF import *
from Defs_por_estado.TAG_DEF import *
from Defs_por_estado.TEXT_DEF import *
from Defs_por_estado.VARIAVEL_DEF import *
from Defs_por_estado.OPENPAR_def import *
from Defs_por_estado.IFSTATE_DEF import *

states = (
    ('openPar', 'exclusive'),
    ('tag', 'exclusive'),
    ('text', 'exclusive'),
    ('id', 'exclusive'),
    ('ponto', 'exclusive'),
    ('variavel', 'exclusive'),
    ('ifstate', 'exclusive')
)

tokens = [
    'NEWLINE',
    'SPACE',
    'OPAR',
    'CPAR',
    'VAR',
    'VARNAME',
    'VARVALUE',
    'ID',
    'CLASS',
    'INDENTATION',
    'IF',
    'ELSE',
    'TAG',
    'DOT',
    'COMMENT',
    'EQUAL'
]

def t_ANY_error(t):
    print("---------------------->Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

pug_code = """
html(lang="en")
    head
        - var pageTitle = "ola"
        title= pageTitle
        script(type='text/javascript').
            if (foo) bar(1 + 5)
    body
        h1 Pug - node template engine
        #container.col
            if youAreUsingPug
                p You are amazing
            else
                p Get on it!
            p.
                Pug is a terse and simple templating language with a
                strong focus on performance and powerful features
            p
            if youAreUsingPug == False
                p ola
"""
text2 = """
html(lang="en")
    head
        title= pageTitle
        script(type='text/javascript').
            if (foo) bar(1 + 5)
    body
        h1 Pug - node template engine
        #container.col"""

lexer = lex.lex()
lexer.ident_linhaAntes = 0
lexer.ident_linhaAtual = 0
"""
lexer.input(pug_code)

for tok in lexer:
    print(tok)
"""

