def t_tag_NEWLINE(t):
    r'\n'
    t.lexer.begin('indentation')
    return t


def t_tag_EQUALS(t):
    r'\='
    t.lexer.begin('attribute')
    return t

def t_tag_SPACE(t):
    r'\ '


def t_tag_TEXT(t):
    r'[\w\!\-]+(\ [\w\!\-]+)*'
    t.lexer.begin('text')
    return t


def t_tag_DOT(t):
    r'\.'
    t.lexer.paiponto = t.lexer.atual
    #print("defini o pai ponto como"+str(paiponto))
    t.lexer.begin('ponto')
    return t


def t_tag_OPAR(t):
    r'\('
    t.lexer.begin('attribute')
    return t
