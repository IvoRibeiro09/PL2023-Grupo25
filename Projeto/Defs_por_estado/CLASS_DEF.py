def t_class_CLASS(t):
    r'\w+'
    return t


def t_class_SPACE(t):
    r'[\ ]'
    t.lexer.begin('text')


def t_class_NEWLINE(t):
    r'\n'
    #print("pushei no class_newline"+str(atual))

    t.lexer.begin('indentation')
    return t
