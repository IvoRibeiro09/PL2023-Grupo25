from Defs_por_estado.new_lexer import *

def main():

    f = open("pug_html.txt", "r")
    lexer.input(f.read())

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()
