def t_indentation_VAR(t):
    r'\-\ var'
    t.lexer.begin('variavel')
    return t


def t_indentation_IF(t):
    r'if'
    t.lexer.begin('text')
    return t


def t_indentation_ELSE(t):
    r'else'
    t.lexer.begin('text')
    return t


def t_indentation_INDENTATION(t):
    r'[\t|\ ]+'
    t.lexer.atual = len(t.value)
    return t


def t_indentation_TAG(t):
    r'[a-z0-9]+'
    t.lexer.begin('tag')
    return t


def t_indentation_TEXT(t):
    r'[\w]+(\ [\w]+)*'
    t.lexer.begin('text')
    return t


def t_indentation_CARDINAL(t):
    r'[\#]+'
    t.lexer.begin('id')
    return t

def t_indentation_SPACE(t):
    r'[\ ]+'
    t.lexer.begin('text')
    return t
