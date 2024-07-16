#desafio 07: Crie um programa onde o usuário digita uma expressão qualquer que use parenteses. 
    #Seu aplicativo deverá analisar se a expressão passada está com os parêntesis abertos a fechados na ordem correta.

expression = str(input('Digite a expressão:')).strip().upper().split()
expression = ''.join(expression)

pilha = []

for position, value in enumerate(expression):
    if value == '(':
        pilha.append('(')
    if value == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é VÁLIDA.')
else:
    print('Sua expressão é INVÁLIDA.')
        


