def t_ifstate_VARNAME(t):
    r'[\w]+'
    return t


t_ifstate_ignore = r' '


def t_ifstate_EQUAL(t):
    r'\=+'
    t.lexer.begin("text")
    return t


def t_ifstate_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t
