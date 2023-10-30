from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

import csv

# Configurações de conexão com o banco de dados
db_host = "10.0.0.173"  # Endereço IP do servidor PostgreSQL...
db_port = "5432"       
db_name = "etl-database"   
db_user = "postgres"  
db_password = "root"

# Crie uma conexão com o banco de dados
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

# Crie uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Defina o modelo da tabela
Base = declarative_base()

class  DataMeliuz(Base):
    __tablename__ = 'DataMeliuz'
#N_total_vendas,N_vendas_pendentes,N_vendas_confirmadas,N_vendas_canceladas,
# N_reclamacoes_porcompra_pendente,N_reclamacoes_porcompra_cancelada
    id = Column(Integer, primary_key=True)
    Parceiro = Column(String(50))
    Categoria = Column(String(50))
    Mes = Column(Date)
    N_total_vendas= Column(Integer)
    N_vendas_pendentes = Column(Integer)
    N_vendas_confirmadas = Column(Integer)
    N_vendas_canceladas = Column(Integer)
    N_reclamacoes_porcompra_pendente = Column(Integer)
    N_reclamacoes_porcompra_cancelada = Column(Integer)
    Taxa_validacao = Column(Float)
    Taxa_confirmacao = Column(Float)
    Volume_reclamacoes = Column(Integer)
    Taxa_compras_pendentes = Column(Float)
    Reclamacoes_porvenda_confirmada = Column(Float)
    

# Crie a tabela no banco de dados
Base.metadata.create_all(engine)

def convert_to_date(mes_ano):
    year, month = map(int, mes_ano.split('-'))
    return datetime(year, month, 1)
csv_file = 'basemeliuz.csv'

try:
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar o cabeçalho do CSV
        for row in reader:
            mes_ano = row[2]
            data = convert_to_date(mes_ano)
            Base_data = DataMeliuz(
                Parceiro = row[0],
                Categoria = row[1],
                Mes = data,
                N_total_vendas= int(row[3]),
                N_vendas_pendentes = int(row[4]),
                N_vendas_confirmadas = int(row[5]),
                N_vendas_canceladas = int(row[6]),
                N_reclamacoes_porcompra_pendente = int(row[7]),
                N_reclamacoes_porcompra_cancelada = int(row[8]),
                Taxa_validacao = float(row[9]),
                Taxa_confirmacao = float(row[10]),
                Volume_reclamacoes = int(row[11]),
                Taxa_compras_pendentes = float(row[12]),
                Reclamacoes_porvenda_confirmada = float(row[13])
            )
            session.add(Base_data)
        
        session.commit()
        print("Commit successful")

except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
