def t_variavel_SPACE(t):
    r'\ '


def t_variavel_TEXT(t):
    r'[\w\-\,\.]+'
    return t


def t_variavel_EQUAL(t):
    r'\='
    return t


def t_variavel_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t
