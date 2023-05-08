from new_lexer import *
def main():
    lexer = lex.lex()
    lexer.input(pug_code)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()