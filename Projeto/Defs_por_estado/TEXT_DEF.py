def t_text_VARVALUE(t):
    r'((?!\n|\.\n|\)).)+'
    t.lexer.begin('openPar')
    return t


t_text_ignore = r' '
