import pandas as pd

# Carregue os dois arquivos CSV em DataFrames
df1 = pd.read_csv('basecsvnova.csv')
df2 = pd.read_csv('base_atualizada_meliuz.csv')

# Compare os DataFrames e encontre as diferenças
diferencas = df1.merge(df2, on='chave', how='outer', indicator=True).query('_merge != "both"')

# As diferenças podem ser acessadas através do DataFrame 'diferencas'
print(diferencas)
