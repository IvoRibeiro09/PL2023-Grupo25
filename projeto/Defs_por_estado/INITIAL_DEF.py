def t_INITIAL_INDENTATION(t):
    r'[\t|\ ]+'
    return t


def t_INITIAL_IF(t):
    r'if'
    t.lexer.begin('ifstate')
    return t


def t_INITIAL_ELSE(t):
    r'else'
    return t


def t_INITIAL_TAG(t):
    r'[a-z0-9]+'
    t.lexer.begin('tag')
    return t


def t_INITIAL_VAR(t):
    r'\-\ var'
    t.lexer.begin('variavel')
    return t


def t_INITIAL_OPAR(t):
    r'\('
    t.lexer.begin('openPar')
    return t


def t_INITIAL_DOT(t):
    r'\.'
    t.lexer.begin('ponto')
    return t


def t_INITIAL_NEWLINE(t):
    r'\n'
    return t


def t_INITIAL_ID(t):
    r'\#'
    t.lexer.begin('id')
    return t
