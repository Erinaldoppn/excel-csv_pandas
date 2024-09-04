import pandas as pd

# Carrega os dados do arquivo Excel
df = pd.read_excel("C:/Users/Erinaldo/Downloads/relatorio.xlsx")

# Converte o DataFrame em uma lista de dicionários
dados = df.to_dict(orient='records')
