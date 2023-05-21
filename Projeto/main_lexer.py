from Defs_por_estado.new_lexer import *
def main():
    lexer = lex.lex()
    lexer.input(text3)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()
