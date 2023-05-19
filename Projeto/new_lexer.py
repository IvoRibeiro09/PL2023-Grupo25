from ply import lex

states =(
    ('indentation','exclusive'),
    ('tag','exclusive'),
    ('text','exclusive'),
    ('attribute','exclusive'),
    ('id','exclusive'),
    ('class','exclusive'),
    ('ponto','exclusive')

)
tokens = [
    'NEWLINE',
    'SPACE',
    'OPAR',
    'CPAR',
    'TEXT',
    'ATTRIBUTE',
    'ID',
    'CLASS',
    'INDENTATION',
    'EQUALS',
    'TAG',
    'CARDINAL',
    'DOT',
    'SPECIAL',
    'IF',
    'ELSE'
]
t_CARDINAL = r'\#'
t_DOT = r'\.'
t_EQUALS = r'='
t_INDENTATION = r'[\t|\ ]+'
t_NEWLINE = r'\n'
t_SPACE = r'\ '
t_OPAR = r'\('
t_CPAR = r'\)'
t_TEXT = r'[\w"\=\'\/\+\-\ \!\?\,]+'
t_ATTRIBUTE = r'[\w"\'\/\+\-\#\ ]+'
t_ID = r'\w+'
t_CLASS = r'\w+'
t_TAG = r'[a-z0-9]+'
t_SPECIAL=r'[\w"\=\'\/\+\-\ \!\?\,]+'
t_IF=r'if'
t_ELSE=r'else'


global atual
atual=0
global paiponto
paiponto=0



def t_INITIAL_INDENTATION(t):
    r'[\t|\ ]+'
    t.lexer.begin('indentation')
    return t
def t_INITIAL_TAG(t):
    r'[a-z0-9]+'
    t.lexer.begin('tag')
    return t


def t_indentation_INDENTATION(t):
    r'[\t|\ ]+'

    #print(len(t.value))
    global atual
    atual= len(t.value)
    #arr.append(atual)
    #print(arr)
    return t

def t_indentation_IF(t):
    r'if'
    t.lexer.begin('attribute')
    return t


def t_indentation_TAG(t):
    r'[a-z0-9]+'
    t.lexer.begin('tag')
    return t
def t_indentation_TEXT(t):
    r'[\w"\=\'\/\+\-\!\?\,]+'
    t.lexer.begin('text')
    return t
def t_indentation_CARDINAL(t):
    r'[\#]+'
    t.lexer.begin('id')
    return t

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

def t_indentation_SPACE(t):
    r'[\ ]+'
    t.lexer.begin('text')
    return t


def t_tag_NEWLINE(t):
    r'\n'
    #print("pushei no tag_newline"+str(atual))
    t.lexer.begin('indentation')
    return t
def t_tag_EQUALS(t):
    r'\='
    t.lexer.begin('attribute')
    return t
def t_tag_TEXT(t):
    r'[\w"\=\'\/\+\-\ \!\?\,]+'
    t.lexer.begin('text')
    return t
def t_tag_DOT(t):
    r'\.'
    global paiponto
    paiponto=atual
    #print("defini o pai ponto como"+str(paiponto))
    t.lexer.begin('ponto')
    return t
"""aqui alterei"""

def t_ponto_INDENTATION(t):
    r'[\t|\ ]+'

    global atual
    atual=len(t.value)

    #print("paiponto:"+str(paiponto))
    if (len(t.value)<=paiponto):
        print("volta para tras")
        t.lexer.begin('indentation')
        return t
    else :
        return t




def t_ponto_SPECIAL(t):
    r'[\w"\=\'\/\+\-\ \!\?\,\)\(\[\]]+'
    return t
def t_ponto_NEWLINE(t):
    r'\n'
    return t




"""alterei"""




def t_tag_OPAR(t):
    r'\('
    t.lexer.begin('attribute')
    return t

def t_attribute_ATTRIBUTE(t):
    r'[\w"\=\'\/\.\+\-\#\ ]+'
    return t


def t_attribute_CPAR(t):
    r'\)'
    t.lexer.begin('tag')
    return t

def t_attribute_NEWLINE(t):
    r'\n'
    #print("pushei no atributo_newline"+str(atual))

    t.lexer.begin('indentation')
    return t


def t_text_SPACE(t):
    r'\ '

def t_text_TEXT(t):
    r'[\w"\=\'\/\.\+\-\ \!\?\,]+'
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
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

pug_code = """
html(lang="en")
    head
        title= pageTitle
        script(type='text/javascript').
            if (foo) bar(1 + 5)
    body
        h1 Pug - node template engine
        #container.col
            if youAreUsingPug
                p You are amazing
            else
                p Get on it!
            p.
                Pug is a terse and simple templating language with a
                strong focus on performance and powerful features
              a
            a
            a.
                aaaa
            b
"""
lexer = lex.lex()
'''
def main():
    lexer = lex.lex()
    lexer.input(pug_code)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()
'''
text3="""
html(lang="en")
    head
         script(type='text/javascript').
            if (foo) bar(1 + 5)
"""