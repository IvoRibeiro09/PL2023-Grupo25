import ply.yacc as yac
from new_lexer import tokens
from CLASSE import *

arr=[]

def p_html(p):
    '''html : blocks '''
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
    '''line : initblock
            | initialine
            | normal_line
            | cardinaline'''
def p_initblock(p):
    '''initblock : INDENTATION TAG novalinha '''
    p[0]= p[2]
    #print(len(p[1]))
    a= Values()
    a.setTag(p[2])
    a.setPosicao(len(p[1]))
    a.setAtributo("")
    arr.append(a)
    print("initblock:"+p[0])




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
    #print("initialine:"+p[0])



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
                    | INDENTATION TAG EQUALS ATTRIBUTE novalinha"""
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
"""
text2="""
html(lang="en")
     body
         title= pageTitle
         p asda
         p a
         p a
         h1 Pug - node template engine
         #container.col
     head
           p asasa
           p aaaaa
"""
parser = yac.yacc()
print(parser.parse(text2))

print("Arr:---------")


pospai=0;
for i in arr:
    posat=i.getPosicao()

    print("-------------------------")
    i.print()
    print("-------------------------")


def gerarEspacos(n):
    return " " * n
"""REVER ISTO N T ABEM"""
indent_level = 0
tag_stack = []
html_string = ""

for line in arr:
    tag = line.getTag()
    attribute = line.getAtributo()
    content=line.getConteudo()
    indentation = line.getPosicao()

    while len(tag_stack) > 0 and indentation <= tag_stack[-1].getPosicao():
        last_tag = tag_stack.pop()
        html_string += f"</{last_tag.getTag()}>\n"

    if indentation > indent_level:
        tag_stack.append(line)
        html_string += f"{gerarEspacos(indent_level)}<{tag} {attribute}>{content}\n"
        indent_level += 1
    elif indentation < indent_level:
        if len(tag_stack) > 0:
            tag_stack.pop()
        html_string += f"</{tag}>\n"
        indent_level -= 1
    else:
        html_string += f"<{tag} {attribute}>{content}</{tag}>"

while len(tag_stack) > 0:
    last_tag = tag_stack.pop()
    html_string += f"</{last_tag.getTag()}>"

print(html_string)


