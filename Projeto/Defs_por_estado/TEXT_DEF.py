def t_text_SPACE(t):
    r'\ '


def t_text_TEXT(t):
    r'[\w]+(\ [\w]+)*'
    return t


def t_text_OPAR(t):
    r'\('
    t.lexer.begin('attribute')
    return t


def t_text_CPAR(t):
    r'\)'
    t.lexer.begin('text')
    return t


def t_text_NEWLINE(t):
    r'\n'
    #print("pushei no text_newline"+str(atual))
    t.lexer.begin('indentation')
    return t
