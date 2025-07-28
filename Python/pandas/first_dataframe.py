import pandas as pd
#from IPython.display import display

vendas = {
    'data': ['25/07/2025', '11/11/2024'],
    'valor': [500, 300],
    'produtos': ['arroz', 'feijão'],
    'qtd': [40, 60],
}

vendas_df = pd.DataFrame(vendas)
print(vendas_df)
