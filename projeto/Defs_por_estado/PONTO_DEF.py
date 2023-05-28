def t_ponto_INDENTATION(t):
    r'[\t|\ ]+'
    t.lexer.ident_linhaAntes = t.lexer.ident_linhaAtual
    t.lexer.ident_linhaAtual = len(t.value)
    if t.lexer.ident_linhaAntes > t.lexer.ident_linhaAtual:
        t.lexer.ident_linhaAntes = 0
        t.lexer.ident_linhaAtual = 0
        t.lexer.begin('INITIAL')
    return t


def t_ponto_COMMENT(t):
    r'[\S\ ]+'
    return t


def t_ponto_NEWLINE(t):
    r'\n'
    return t
