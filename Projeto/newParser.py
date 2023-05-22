
import re

import ply.yacc as yac
from Defs_por_estado.new_lexer import tokens
from CLASSE import *

variaveis = []
arr = []


def p_html(p):
    '''html : novalinha blocks
            | blocks '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_blocks(p):
    '''blocks : blocks block
            | block '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]


# aqui tenho de definir o bloco como um initblock e content, ou so init block
def p_block(p):
    '''block : lines
        '''
    if len(p) == 2:
        p[0] = f"<{p[1]}>" + f"</{p[1]}>"
    # print("Varylines:" + str(p[0]))


def p_lines(p):
    '''lines : lines line
             | line '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]


def p_line(p):
    '''line : initialine
            | initblock
            | normal_line
            | cardinaline
            | specialine
            | dotline
            | variableline
            | ifline
            | elseline'''


def p_initblock(p):
    '''initblock : INDENTATION TAG novalinha '''
    p[0] = p[2]
    # print(len(p[1]))
    a = Values()
    a.setTag(p[2])
    a.setPosicao(len(p[1]))
    a.setAtributo("")
    arr.append(a)
    # print("initblock:"+p[0])


def p_initialine(p):
    '''initialine : TAG OPAR ATTRIBUTE CPAR novalinha
                  | TAG novalinha'''
    if len(p) == 3:
        p[0] = f"{p[1]}"
        a = Values()
        a.setTag(p[1])
        a.setPosicao(0)
        a.setAtributo("")
        arr.append(a)
    elif len(p) == 6:
        p[0] = f"<{p[1]}>" + p[2] + p[3] + p[4] + p[5]
        a = Values()
        a.setTag(p[1])
        a.setPosicao(0)
        a.setAtributo(p[3])
        arr.append(a)


def p_cardinaline(p):
    '''cardinaline : INDENTATION CARDINAL ID novalinha
                   | INDENTATION CARDINAL ID DOT CLASS novalinha'''
    if len(p) == 5:
        a = Values()
        a.setTag("div")
        a.setPosicao(len(p[1]))
        a.setAtributo(f'id="{p[3]}"')
        arr.append(a)
    elif len(p) == 7:
        a = Values()
        a.setTag("div")
        a.setPosicao(len(p[1]))
        a.setAtributo(f'class="{p[5]}" id="{p[3]}"')
        arr.append(a)


def p_normal_line(p):
    '''normal_line : INDENTATION TAG TEXT novalinha
                    | INDENTATION TAG EQUALS ATTRIBUTE novalinha
                    | INDENTATION TAG OPAR ATTRIBUTE CPAR novalinha'''
    if len(p) == 5:
        p[0] = f"<{p[2]}>" + f"{p[3]}" + "</p>"
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
        a.setVariavel(p[4])
        arr.append(a)
    elif len(p) == 7:
        p[0] = f"<{p[2]}>" + f"{p[3]}"
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo(p[4])
        arr.append(a)


def p_specialine(p):
    '''specialine : INDENTATION TAG DOT novalinha
                  | INDENTATION TAG OPAR ATTRIBUTE CPAR DOT novalinha'''
    if len(p) == 5:
        p[0] = p[1] + p[2] + p[3]
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo("")
        a.setConteudo("")
        a.setComment(True)
        arr.append(a)
    elif len(p) == 8:
        p[0] = p[1] + p[2] + p[3]
        a = Values()
        a.setTag(p[2])
        a.setPosicao(len(p[1]))
        a.setAtributo(p[4])
        a.setConteudo("")
        a.setComment(True)
        arr.append(a)
    # print("specialine|" + p[0] + "|")
    return p[0]


def p_dotline(p):
    '''dotline : INDENTATION SPECIAL novalinha'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
        ax = arr[-1].getConteudo()
        ax += p[0]
        arr[-1].setConteudo(ax)
        print("ax|" + ax + "|")
    # print("dotline|" + p[0] + "|")
    return p[0]


# por os outros casos
def p_variableline(p):
    '''variableline : INDENTATION VAR TEXT EQUAL TEXT novalinha'''
    if len(p) == 7:
        dicionario = {'nome': str(p[3]), 'valor': str(p[5])}
        variaveis.append(dicionario)
    # print("varibleline|")
    # print(variable)
    return p[0]


def p_ifline(p):
    '''ifline : INDENTATION IF TEXT novalinha'''
    if len(p) == 5:
        # print(p[3])
        a = Values()
        a.setPosicao(len(p[1]))
        a.setIF(1)
        a.setIfContent(p[3])
        arr.append(a)
    # print("IFLINE|")
    return p[0]


def p_elseline(p):
    '''elseline : INDENTATION ELSE novalinha'''
    if len(p) == 4:
        a = Values()
        a.setPosicao(len(p[1]))
        a.setIF(-1)
        arr.append(a)
        # print("ELSEWLINE|")
    return p[0]


def p_novalinha(p):
    '''novalinha : NEWLINE'''
    p[0] = p[1]


def p_error(p):
    print(p)
    print("Erro sintático no input!")


text = """
html(lang="en")
    head
        - var pageTitle = ola
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

parser = yac.yacc()
print(parser.parse(text))

print("Arr:---------")

pospai = 0;
for i in arr:
    posat = i.getPosicao()

    print("-------------------------")
    i.print()
    print("-------------------------")


def espacos(n):
    return " " * n


def validar(nome, valor):
    for variavel in variaveis:
        if variavel['nome'] == nome and variavel['valor'] == valor:
            return 0

    return 1


pos = []
pospos = []
p = 0

def getAtribute(str):
    if str:
        return " "+str
    else:
        return ""
def draw(atual, negpos):
    print(espacos(atual.getPosicao()-negpos) + "<" + atual.getTag() + getAtribute(atual.getAtributo()) + ">")
    pos.append(atual.getTag())
    pospos.append(atual.getPosicao())
    if atual.getVariavel() != "":
        for var in variaveis:
            if var['nome'] == atual.getVariavel():
                print(espacos(atual.getPosicao() + 4-negpos) + var['valor'])
    if atual.getConteudo() != "" and atual.getComment() == False:
        print(espacos(atual.getPosicao() + 4-negpos) + atual.getConteudo())
    elif atual.getConteudo() != "" and atual.getComment():
        print(atual.getConteudo(), end='')
    if p + 1 < len(arr) and atual.getPosicao() >= arr[p + 1].getPosicao():
        print(espacos(pospos.pop()-negpos) + "</" + pos.pop() + ">")
        if (atual.getPosicao()-negpos) > arr[p + 1].getPosicao() and len(pos) > 0:
            print(espacos(pospos.pop()-negpos) + "</" + pos.pop() + ">")

def name_value(str):
    n_arr = re.split(r'\ *=+\ *', str)
    if len(n_arr) < 2:
        n_arr.append("True")
    return n_arr
pprint = 0
while p < len(arr):
    atual = arr[p]
    if atual.getIf() == 1:
        nameValue = name_value(atual.getIfContent())
        pprint = validar(nameValue[0], nameValue[1])
        identacao_if = atual.getPosicao()
        while p + 1 < len(arr) and arr[p + 1].getPosicao() > identacao_if:
            p = p + 1
            atual = arr[p]
            if pprint == 0:
                draw(atual, 4)
    elif atual.getIf() == -1:
        identacao_if = atual.getPosicao()
        while p + 1 < len(arr) and arr[p + 1].getPosicao() > identacao_if:
            p = p + 1
            atual = arr[p]
            if pprint == 1:
                draw(atual, 4)
    else:
        draw(atual, 0)
    p = p + 1
while pos:
    print(espacos(pospos.pop()) + "</" + pos.pop() + ">")
