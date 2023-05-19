import ply.yacc as yac
from new_lexer import tokens
from CLASSE import *

arr=[]

def p_html(p):
    '''html : novalinha blocks
            | blocks '''
    if len(p)==3:
        p[0] = p[2]
    else :
        p[0]=p[1]

"""line :  espacos TAG novalinha
            | TAG OPAR
            | TAG TEXT
            | novalinha"""
"""
line : initblock
            | initialine
"""

def p_blocks(p):
    '''blocks : blocks block
            | block '''
    if len(p)==2:
        p[0]=[p[1]]
    elif len(p)==3:
        p[0]=p[1]+[p[2]]


#aqui tenho de definir o bloco como um initblock e content, ou so init block
def p_block(p):
    '''block : lines
        '''
    if len(p) == 2:
        p[0] = f"<{p[1]}>"+f"</{p[1]}>"
    print("Varylines:"+str(p[0]))

def p_lines(p):
    '''lines : lines line
             | line '''
    if len(p)==2:
        p[0]=[p[1]]
    elif len(p)==3:
        p[0]=p[1]+[p[2]]

def p_line(p):
    '''line : initialine
            | initblock
            | normal_line
            | cardinaline
            | specialine
            | dotline '''
def p_initblock(p):
    '''initblock : INDENTATION TAG novalinha '''
    p[0]= p[2]
    #print(len(p[1]))
    a= Values()
    a.setTag(p[2])
    a.setPosicao(len(p[1]))
    a.setAtributo("")
    arr.append(a)
    #print("initblock:"+p[0])



def p_initialine(p):
    '''initialine : TAG OPAR ATTRIBUTE CPAR novalinha
                  | TAG novalinha'''
    if len(p)==3:
        p[0]=f"{p[1]}"
        a = Values()
        a.setTag(p[1])
        a.setPosicao(0)
        a.setAtributo("")
        arr.append(a)
    elif len(p)==6:
        p[0] = f"<{p[1]}>" + p[2]+p[3]+ p[4]+p[5]
        a = Values()
        a.setTag(p[1])
        a.setPosicao(0)
        a.setAtributo(p[3])
        arr.append(a)


def p_cardinaline(p):
    '''cardinaline : INDENTATION CARDINAL ID novalinha
                   | INDENTATION CARDINAL ID DOT CLASS novalinha'''
    if len(p)==5:
        a = Values()
        a.setTag("div")
        a.setPosicao(len(p[1]))
        a.setAtributo(f'id="{p[3]}"')
        arr.append(a)
    elif  len(p)==7:
        print()
        a = Values()
        a.setTag("div")
        a.setPosicao(len(p[1]))
        a.setAtributo(f'class="{p[5]}" id="{p[3]}"')
        arr.append(a)

#aqui ta a apanhar um espaco a mais
def p_normal_line(p):
    """normal_line : INDENTATION TAG TEXT novalinha
                    | INDENTATION TAG EQUALS ATTRIBUTE novalinha
                    | INDENTATION TAG OPAR ATTRIBUTE CPAR novalinha"""
    if len(p) == 5:
        p[0] = f"<{p[2]}>"+f"{p[3]}"+"</p>"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setConteudo(p[3])
        arr.append(a)
    elif len(p) == 6:
        p[0] = f"<{p[2]}>" + f"{p[3]}"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setConteudo(p[4])
        arr.append(a)
    elif len(p) == 7:
        p[0] = f"<{p[2]}>" + f"{p[3]}"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo(p[4])
        arr.append(a)

"""
def p_dotblock(p):
    dotblock : INDENTATION TAG DOT novalinha dotcontent
                | INDENTATION TAG DOT novalinha
    if len(p) == 5:
        print("len=5")
        p[0] = f"<{p[2]}>"+f"{p[3]}"+"</p>"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setConteudo("")
        arr.append(a)
    elif len(p) == 6:
        print("entrei")
        p[0] = f"<{p[2]}>"+f"{p[3]}"+"</p>"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        print("p de 5 no dotblock"+p[5])
        a.setConteudo(p[5])
        arr.append(a)
        print("especial no dotblock")
def p_dotcontent(p):
    dotcontent : dotcontent dotline
                  | dotline

    if len(p)==3:
        print("DOTCONTENT LEN=3")
        #print("P[1="+p[1])
        #print("P[2=" + p[2])
        p[0]=p[1]+p[2]
        print("p de 0|"+p[0]+"|")
    else :
        p[0]=p[1]
        print("dotcontent else")
    return p[0]
"""
def p_specialine(p):
    """specialine : INDENTATION TAG DOT novalinha
                  | INDENTATION TAG OPAR ATTRIBUTE CPAR DOT novalinha"""
    if len(p)==5:
        p[0]=p[1]+p[2]+p[3]
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo("")
        a.setConteudo("")
        arr.append(a)
    elif len(p)==8:
        p[0] = p[1] + p[2] + p[3]
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo(p[4])
        a.setConteudo("")
        arr.append(a)
    print("specialine|"+ p[0]+"|")

    return p[0]

def p_dotline(p):
    """dotline : INDENTATION SPECIAL novalinha"""
    if len(p)==4:
        p[0]=p[1]+p[2]+p[3]
        ax=arr[-1].getConteudo()
        ax+=p[0]
        arr[-1].setConteudo(ax)
        print("ax|"+ax+"|")
    print("dotline|"+ p[0]+"|")
    return p[0]


def p_novalinha(p):
    '''novalinha : NEWLINE'''
    p[0]=p[1]



def p_error(p):
    print(p)
    print("Erro sintático no input!")

text="""
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
            p
                
"""
text2="""
html(lang="en")
     body
         script(type='text/javascript').
            if (foo) bar(1 + 5)
         title= pageTitle
         p asda
         p a
         p a
         h1 Pug - node template engine
         #container.col
     head
           p asasa
           p aaaa
           p.
                aaaaa
                bbbbb
                cccc
           p.
                a
                """

text3="""
html(lang="en")
    head
         script(type='text/javascript').
            if (foo) bar(1 + 5)
"""
parser = yac.yacc()
print(parser.parse(text))

print("Arr:---------")


pospai=0;
for i in arr:
    posat=i.getPosicao()

    print("-------------------------")
    i.print()
    print("-------------------------")


def gerarEspacos(n):
    return " " * n
indent_level = 0
tag_stack = []
html_string = ""

def espacos(n):
    return " " * n

pos = []
pospos = []
p = 0
while p < len(arr):
    atual = arr[p]
    print(espacos(atual.getPosicao()) + "<" + atual.getTag() + " " + atual.getAtributo() + ">")
    pos.append(atual.getTag())
    pospos.append(atual.getPosicao())
    if(atual.getConteudo()):
        print(espacos(atual.getPosicao() + 4) + atual.getConteudo())
    if p+1 < len(arr) and atual.getPosicao() >= arr[p+1].getPosicao():
        print(espacos(pospos.pop()) + "</" + pos.pop() + ">")
        if atual.getPosicao() > arr[p + 1].getPosicao():
            print(espacos(pospos.pop()) + "</" + pos.pop() + ">")
    p = p + 1
while pos:
    print(espacos(pospos.pop()) + "</" + pos.pop() + ">")