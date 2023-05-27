def t_tag_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t


def t_tag_EQUAL(t):
    r'\=+'
    t.lexer.begin('text')
    return t


def t_tag_SPACE(t):
    r'\ '


def t_tag_OPAR(t):
    r'\('
    t.lexer.begin('openPar')
    return t


def t_tag_COMMENT(t):
    r'[\w][\w\ \-\!]*'
    return t


def t_tag_DOT(t):
    r'\.'
    t.lexer.begin('ponto')
    return t
"""<html lang="en">

<head>
    <title>
    </title>
    <script type="text/javascript">
        if (foo) bar(1 + 5)
    </script>
</head>

<body>
    <h1>Pug - node template engine
    </h1>
    <div class="col" id="container">
        <p>
            Get on it!
        </p>
        <p>
            Pug is a terse and simple templating language with a
            strong focus on performance and powerful features
        </p>
        <p>
        </p>
    </div>
</body>

</html>"""
