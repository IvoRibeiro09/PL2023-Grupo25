def t_comentstate_COMMENT(t):
    r'[\S\ ]+'
    return t


def t_comentstate_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t
