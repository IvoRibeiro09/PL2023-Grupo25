def t_INITIAL_INDENTATION(t):
    r'[\t|\ ]+'
    t.lexer.begin('indentation')
    return t


def t_INITIAL_TAG(t):
    r'[a-z0-9]+'
    t.lexer.begin('tag')
    return t


def t_INITIAL_VAR(t):
    r'\-\ var'
    t.lexer.begin('variavel')
    return t


def t_INITIAL_NEWLINE(t):
    r'\n'
    t.lexer.begin('indentation')
    return t


def t_INITIAL_IF(t):
    r'if'
    t.lexer.begin('text')
    return t


def t_INITIAL_ELSE(t):
    r'else'
    return t
