import re
import ply.yacc as yac
from Defs_por_estado.new_lexer import tokens



def espacos(n):
    return " " * n


def closeTag(arr1, arr2, pos):
    string = ""
    while len(arr2) > 0 and pos <= arr2[-1]:
        string += espacos(arr2.pop()) + "</" + arr1.pop() + ">\n"
    return string


def ifvar(dict):
    if 'tagVAR' in dict and dict['tagVAR'] and 'tagVARVALUE' in dict and dict['tagVARVALUE']:
        string = ""
        for n, v in zip(dict['tagVAR'], dict['tagVARVALUE']):
            string += " " + n + "=" + '"' + v + '"'
        return string
    else:
        return ""

def checkvar(dicionario, arr):
    for i in arr:
        if str(dicionario.get('varNAME')) == str(i.get('Nome')) and str(dicionario.get('varVALUE')) == str(i.get('Value')):
            return True
    return False


def check(bool, anterior, pos):
    if bool:
        if anterior >= pos:
            return False
        else:
            return True
    else:
        return bool

def negIndentation(negpos, negposposition, elemento):
    if negpos != 0:
        if elemento['pos'] <= negposposition:
            return 0
    return negpos

def arr_html(arr):
    finalString = ""
    var_arr = []
    pos = []
    pospos = []
    pos_atual = -1
    dontdraw = False
    ifprint = True
    negpos = 0
    negposposition = 0
    for element in arr:
        dontdraw = check(dontdraw, negposposition, element['pos'])
        negpos = negIndentation(negpos, negposposition, element)
        print(str(negpos)+ "  "+str(element))
        pos_atual = element['pos']
        if not dontdraw:
            if 'Var' in element and element['Var']:
                var_arr.append({'Nome': element['Nome'], 'Value': element['Value']})
            elif 'if' in element and element['if']:
                negpos = -4
                negposposition = pos_atual
                if not checkvar(element, var_arr):
                    dontdraw = True
                    ifprint = False
            elif 'else' in element and element['else']:
                negpos = -4
                negposposition = pos_atual
                if ifprint:
                    dontdraw = True
            elif 'tag' in element and element['tag']:
                finalString += closeTag(pos, pospos, pos_atual+negpos)
                pos.append(element['tag'])
                pospos.append(element['pos']+negpos)
                finalString += (espacos(element['pos']+negpos) + "<" + element['tag'] + ifvar(element) + ">\n")
                if 'conteudo' in element and element['conteudo']:
                    finalString += espacos(element['pos'] + 4+negpos) + element['conteudo'] + "\n"
                elif 'var' in element and element['var']:
                    for i in var_arr:
                        if i['Nome'] == element['var']:
                            finalString += espacos(element['pos'] + 4+negpos) + i['Value'] + "\n"
            elif 'conteudo' in element and element['conteudo']:
               finalString += espacos(element['pos']+negpos) + element['conteudo'] + "\n"
    while pos:
        finalString += closeTag(pos, pospos, -1)
    return finalString


def p_pugHTML(p):
    '''pugHTML : pugHTML linhas
                | '''
    if len(p) == 3:
        p[0] = arr_html(p[2])
    else:
        p[0] = ""


def p_linhas(p):
    '''linhas : linhas linha
           | linha'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = [p[1]]


def p_linha(p):
    '''linha : INDENTATION line NEWLINE
            | line NEWLINE
            | NEWLINE'''
    if len(p) == 4:
        p[2]['pos'] = len(p[1])
        p[0] = p[2]
    elif len(p) == 3:
        p[1]['pos'] = 0
        p[0] = p[1]
    else:
        p[0] = {'pos': 0}


def p_line(p):
    '''line : tagline
            | tagdotline
            | trashline
            | cardinalline
            | varline
            | ifline
            | elseline'''
    p[0] = p[1]


def p_elseline(p):
    '''elseline : ELSE '''
    p[0] = {'else': True}


# IF VARNAME EQUAL VARVALUE
def p_ifline(p):
    '''ifline : IF VARNAME EQUAL VARVALUE
                | IF VARNAME'''
    if len(p) == 5:
        p[0] = {'if': True, 'varNAME': p[2], 'varVALUE': p[4]}
    else:
        p[0] = {'if': True, 'varNAME': p[2], 'varVALUE': True}


def p_tagdotline(p):
    '''tagdotline : TAG OPAR VARNAME EQUAL VARVALUE CPAR DOT
                | TAG EQUAL VARVALUE DOT
                | TAG COMMENT DOT
                | TAG DOT'''
    if len(p) == 8:
        p[0] = {'tag': p[1], 'tagVAR': [p[3]], 'tagVARVALUE': [p[5]], 'lixo': True}
    elif len(p) == 5:
        p[0] = {'tag': p[1], 'var': p[3], 'lixo': True}
    elif len(p) == 4:
        p[0] = {'tag': p[1], 'conteudo': p[2], 'lixo': True}
    elif len(p) == 3:
        p[0] = {'tag': p[1], 'lixo': True}


def p_tagline(p):
    '''tagline : TAG OPAR VARNAME EQUAL VARVALUE CPAR
                | TAG EQUAL VARVALUE
                | TAG COMMENT
                | TAG'''
    if len(p) == 7:
        p[0] = {'pos': 0, 'tag': p[1], 'tagVAR': [p[3]], 'tagVARVALUE': [p[5]]}
    elif len(p) == 4:
        p[0] = {'pos': 0, 'tag': p[1], 'var': p[3]}
    elif len(p) == 3:
        p[0] = {'pos': 0, 'tag': p[1], 'conteudo': p[2]}
    elif len(p) == 2:
        p[0] = {'pos': 0, 'tag': p[1]}


def p_trashline(p):
    '''trashline : COMMENT'''
    p[0] = {'conteudo': p[1]}


def p_cardinalline(p):
    '''cardinalline : ID VARVALUE DOT VARVALUE
                    | ID VARVALUE'''
    if len(p) == 5:
        p[0] = {'tag': 'div', 'tagVAR': ['class', 'id'], 'tagVARVALUE': [p[4], p[2]]}
    elif len(p) == 4:
        p[0] = {'tag': 'div', 'tagVAR': 'id', 'tagVARVALUE': p[2]}


def p_varline(p):
    '''varline : VAR VARNAME EQUAL VARVALUE'''
    p[0] = {'Var': True, 'Nome': p[2], 'Value': p[4]}


def p_error(p):
    print(p)
    print("Erro sintático no input!")

text = '''
html(lang="en")
    head
        - var pageTitle = ola Ivo tudo bem?
        - var youAreUsingPug = True
        title= pageTitle
        script(type='text/javascript').
            if (foo) bar(1 + 5)
    body
        p You are amazing
        p Ivo is amazingn
        h1 Pug - node template engine
        #container.col
            if youAreUsingPug == True
                p You are amazing
                p Ivo is amazingn
            else
                p Get on it!
            p.
                Pug is a terse and simple templating language with a
                strong focus on performance and powerful features
            p     
'''
parser = yac.yacc()
print(parser.parse(text, debug=0))

print("Arr:---------")
