def t_id_ID(t):
    r'[\w]+'
    return t


def t_id_SPACE(t):
    r'[\ ]+'
    t.lexer.begin('text')
    return t


def t_id_NEWLINE(t):
    r'\n'
    #print("pushei no id_newline"+str(atual))
    t.lexer.begin('indentation')
    return t


def t_id_DOT(t):
    r'\.'
    t.lexer.begin('class')
    return t
