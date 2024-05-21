nome = str(input('Qual o seu nome?'))

if nome == 'Beatriz': 
    print('Seu nome é muito bonito!')
elif nome == 'Geovana' or nome == 'Dandara':
    print('Seu nome até que é maneirinho.')
elif nome in 'Aimee Jully Estefany Julia':
    print('Você é uma tereziner.')
elif nome in 'Isis Eduarda Luiza Gabriele Maynah':
    print('Você é uma santa moniquer.')
else:
    print('Você não é uma girlie.')

print('Seu nome é {}'.format(nome))