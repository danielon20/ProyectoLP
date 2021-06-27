import lexi

lexer = lexi.goLexer()

data = '0000'

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
