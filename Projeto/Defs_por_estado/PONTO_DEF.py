def t_ponto_INDENTATION(t):
    r'[\t|\ ]+'
    t.lexer.atual = len(t.value)

    #print("paiponto:"+str(paiponto))
    if (len(t.value)<= t.lexer.paiponto):
        print("volta para tras")
        t.lexer.begin('indentation')
        return t
    else:
        return t

def t_ponto_SPECIAL(t):
    r'[\S]+(\ [\S]+)*'
    return t

def t_ponto_NEWLINE(t):
    r'\n'
    return t

