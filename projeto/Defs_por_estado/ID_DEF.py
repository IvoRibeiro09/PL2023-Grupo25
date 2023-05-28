def t_id_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t


def t_id_DOT(t):
    r'\.'
    return t


def t_id_VARVALUE(t):
    r'[\w]+'
    return t
