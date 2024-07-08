#desafio 02: Crie uma tupla preenchida com os 20 primeiros colocados da Tabala do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    #A) Apenas os 5 primeiros colocados.
    #B) Os últimos 4 colocados da tabela.
    #C) Uma lista com os times em ordem alfabética.
    #D) Em que posição na tabela está o time da Chapecoense.

tabela = ("Vasco da Gama", "Corinthians", "Palmeiras", "São Paulo", "Santos", "Internacional", "Grêmio", "Cruzeiro", "Atlético Mineiro", "Fluminense", "Botafogo", "Flamengo", "Bahia", "Sport Recife", "Ceará", "Fortaleza", "Athletico Paranaense", "Coritiba", "Goiás", "Chapecoense")

print(f'A Tabela de times do Brasileirão é: {tabela}')
print('=-='*10)
print(f'Os 5 primeiros colocados são: {tabela[0:6]}')
print('=-='*10)
print(f'Os últimos 4 colocados da tabela: {tabela[-4:]}')
print('=-='*10)
print(f'Times em orem alfabética: {sorted(tabela)}')
print('=-='*10)
print(f'A Chapecoense está na {tabela.index("Chapecoense")}ª posição')
print('=-='*10)