def t_ifstate_VARNAME(t):
    r'[\w]+'
    return t


def t_ifstate_SPACE(t):
    r'\ '


def t_ifstate_EQUAL(t):
    r'\=+'
    t.lexer.begin("text")
    return t


def t_ifstate_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t
