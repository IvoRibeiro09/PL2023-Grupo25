from ply import lex

from Defs_por_estado.ID_DEF import *
from Defs_por_estado.ATTRIBUTE_DEF import *
from Defs_por_estado.CLASS_DEF import *
from Defs_por_estado.INITIAL_DEF import *
from Defs_por_estado.INDENTATION_DEF import *
from Defs_por_estado.PONTO_DEF import *
from Defs_por_estado.TAG_DEF import *
from Defs_por_estado.TEXT_DEF import *
from Defs_por_estado.VARIAVEL_DEF import *

states = (
    ('indentation', 'exclusive'),
    ('tag', 'exclusive'),
    ('text', 'exclusive'),
    ('attribute', 'exclusive'),
    ('id', 'exclusive'),
    ('class', 'exclusive'),
    ('ponto', 'exclusive'),
    ('variavel', 'exclusive')
)

tokens = [
    'NEWLINE',
    'SPACE',
    'OPAR',
    'CPAR',
    'TEXT',
    'ATTRIBUTE',
    'ID',
    'CLASS',
    'INDENTATION',
    'EQUALS',
    'IF',
    'ELSE',
    'TAG',
    'CARDINAL',
    'DOT',
    'SPECIAL',
    'VAR',
    'EQUAL'
]

def t_ANY_error(t):
    print("---------------------->Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

pug_code = """
html(lang="en")
    head
        title= pageTitle
        script(type='text/javascript').
            if (foo) bar(1 + 5)
    body
        h1 Pug - node template engine
        #container.col
            - var youAreUsingPug = True
            if youAreUsingPug 
                p You are amazing
            else
                p Get on it!
            p.
                Pug is a terse and simple templating language with a
                strong focus on performance and powerful features
              a
            a
            a.
                aaaa
            b
"""

'''
def main():
    lexer = lex.lex()
    lexer.input(pug_code)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()
'''
text3 = """
html(lang="en")
    - var aaa = True
     if youAreUsingPug
        p You are amazing
     else
        p Get on it!
"""

lexer = lex.lex()
lexer.paiponto = 0
lexer.atual = 0
