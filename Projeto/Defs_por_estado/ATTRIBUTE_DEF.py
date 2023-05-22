def t_attribute_SPACE(t):
    r'\ '


def t_attribute_ATTRIBUTE(t):
    r'[\w\"\=\'\/]+(\ [\w\"\=\'\/]+)*'
    return t


def t_attribute_CPAR(t):
    r'\)'
    t.lexer.begin('tag')
    return t


def t_attribute_NEWLINE(t):
    r'\n'
    t.lexer.begin('indentation')
    return t
