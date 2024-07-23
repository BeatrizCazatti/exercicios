pessoas = {'nome': 'Beatriz', 'idade': 18, 'sexo': 'F'}

print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())

del pessoas['sexo']
pessoas['peso'] = 64.4

for k, v in pessoas.items():
    print(f'{k} = {v}')
