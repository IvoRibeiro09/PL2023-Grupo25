def t_variavel_SPACE(t):
    r'\ '


def t_variavel_VARNAME(t):
    r'[A-Z|a-z]+'
    return t


def t_variavel_EQUAL(t):
    r'\=+'
    t.lexer.begin('text')
    return t


def t_variavel_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t
