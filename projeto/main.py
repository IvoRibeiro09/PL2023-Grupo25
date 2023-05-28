from projeto.newParser import *
from Defs_por_estado.new_lexer import *

def main():
    i=1
    while(i!=0):
        print()
        print("############## PL2023 Grupo 25########################")
        print("# Insira uma opção:                                  #")
        print("# 1-> Ações com o Lexer                              #")
        print("# 2-> Ações com o Parser                             #")
        print("#                                                    #")
        print("# 0-> Sair                                           #")
        print("######################################################")

        i = input()


        if i =="1":
            print("Insira o nome do arquivo de Input")
            arq = input()
            f = open(arq, "r")
            if f:
                lexer.input(f.read())
                for tok in lexer:
                    print(tok)
                f.close()
        elif i=="2" :
            print("Insira o nome do arquivo de Input")
            arq = input()
            f = open(arq, "r")
            if f:
                print("Insira o nome para o ficheiro de output")
                newname=input()
                #print(f.read())
                novo=f.read()
                p = parser.parse(novo, debug=0)
                print(p)
                out = open(newname, "w")
                out.write(p)
                out.close()
                f.close()

        else:
            i=0
            print("Invalid character")


if __name__ == '__main__':
    main()
