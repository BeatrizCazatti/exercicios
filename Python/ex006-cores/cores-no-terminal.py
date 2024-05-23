#ANSI(style; text; back)
#style: 0-none, 1-bold, 4-underline, 7-negative
#text: 30-branco, 31-vermelho, 32-verde, 33-amarelo, 34-azul, 35-roxo, 36-ciano, 37-preto
#back: 40-branco, 41-vermelho, 42-verde, 43-amarelo, 44-azul, 45-roxo, 46-ciano, 47-preto

t1 = 'vasco'
t2 = 'fluminense'
t3 = 'flamengo'
print('\033[30;47m {} \033[ \033[31;42m {} \033[37;41m {}\033[m'.format(t1, t2, t3))