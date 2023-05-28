def t_tag_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t


def t_tag_EQUAL(t):
    r'\=+'
    t.lexer.begin('text')
    return t


t_tag_ignore = r' '


def t_tag_OPAR(t):
    r'\('
    t.lexer.begin('openPar')
    return t


def t_tag_COMMENT(t):
    r'((?!\n|\.\n).)+'
    return t


def t_tag_DOT(t):
    r'\.'
    t.lexer.begin('ponto')
    return t

