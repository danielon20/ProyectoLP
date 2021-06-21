import lexi

lexer = lexi.goLexer()

data = 'if=5'
 
 # Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
