import pandas as pd

csv_file = 'basemeliuz.csv'
df = pd.read_csv(csv_file)

# Renomear a coluna 'MÊs' para 'data' e 'Nº Total de vendas' para 'N_total_vendas'
df = df.rename(columns={'Mês': 'Mes', 'Nº total de vendas': 'N_total_vendas', 'Nº de vendas pendentes': 'N_vendas_pendentes', 'Nº de vendas confirmadas': 'N_vendas_confirmadas', 'Nº de vendas canceladas' : 'N_vendas_canceladas', 'Nº de reclamações por compra pendente': 'N_reclamacoes_porcompra_pendente', 'Nº de reclamações por compra cancelada': 'N_reclamacoes_porcompra_cancelada'})

df['Taxa_validacao'] = (df['N_vendas_confirmadas'] + df['N_vendas_canceladas']) / df['N_total_vendas']
df['Taxa_confirmacao'] =  df['N_vendas_confirmadas'] / df['N_total_vendas'] 
df['Volume_reclamacoes'] = df['N_reclamacoes_porcompra_cancelada'] + df['N_reclamacoes_porcompra_pendente']
df['Taxa_compras_pendentes'] = df['N_vendas_pendentes'] / df['N_total_vendas']
df['Reclamacoes_porvenda_confirmada'] = (df['N_reclamacoes_porcompra_cancelada'] + df['N_reclamacoes_porcompra_pendente']) / df['N_vendas_confirmadas']
# Salvando o arquivo CSV com encoding 'utf-8'
df.to_csv(csv_file, index=False,  encoding = 'UTF-8', float_format='%.3f')

print(f'Arquivo CSV salvo como {csv_file} com encoding UTF-8')