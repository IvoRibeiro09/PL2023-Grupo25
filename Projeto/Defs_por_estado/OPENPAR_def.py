def t_openPar_SPACE(t):
    r'\ '


def t_openPar_VARNAME(t):
    r'[\w|_]+'
    return t


def t_openPar_EQUAL(t):
    r'\=+'
    t.lexer.begin('text')
    return t


def t_openPar_CPAR(t):
    r'\)'
    t.lexer.begin('INITIAL')
    return t


def t_openPar_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    return t
