def t_text_VARVALUE(t):
    r'[\w\"\-\_\'\/]+'
    t.lexer.begin('openPar')
    return t


def t_text_SPACE(t):
    r'\ '
