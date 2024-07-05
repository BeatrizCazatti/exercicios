nome = input('Nome:')
idade = float(input('Idade:'))

print('Meu nome é:',nome,'tenho', idade, 'anos')
print(f'Meu nome é:{nome:^20} tenho {idade:2f} anos')
print('Meu nome é:{} tenho {} anos'.format(nome, idade))
#Com o uso de várias strings com o separador ‘sep’ indicando a quebra de linha entre cada uma delas, cada string será impressa com espaçamentos e quebras de linha.
print('Meu nome é:',nome,'Tenho',idade, 'anos.',sep='\n')
      