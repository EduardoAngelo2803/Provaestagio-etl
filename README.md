# Instruções para Conectar um Banco de Dados ao Metabase Usando Docker Desktop e Windows
Este README descreve o processo de configuração e execução do Metabase em conjunto com um banco de dados PostgreSQL usando Docker. O Metabase é uma ferramenta de visualização de dados que permite criar painéis e relatórios a partir de fontes de dados. Caso você esteja usando **wsl** ou **linux**, ao executar o **script run_all.sh**, o processo é automatizado! Para isso, é necessário criar um arquivo chamada ip_adress.txt, e colocá-lo na mesma pasta do seu projeto, junto com o arquivo csv, e os jobs.py

## Pré-requisitos
Antes de começar, certifique-se de ter instalado os seguintes componentes:
 
**Docker Desktop:** Certifique-se de que o Docker Desktop esteja instalado em seu sistema. Você pode baixá-lo em Docker Desktop.

**Python:** É necessário ter o Python instalado. Recomendamos a versão 3.10 ou 3.11, pois a versão 3.12 pode não ser compatível com a biblioteca psycopg2, que será necessária.

**Bibliotecas Python:** Instale as seguintes bibliotecas Python executando os seguintes comandos no terminal:

```
pip install sqlalchemy
pip install psycopg2
pip install pandas
```
## Configurando o Banco de Dados PostgreSQL
Antes de executar o Metabase, você deve configurar um banco de dados PostgreSQL. Siga estas etapas:

1. Certifique-se de que o arquivo de banco de dados que você deseja usar esteja na mesma pasta dos scripts job_1.py e job_2.py.

2. Inicialize o Docker Desktop.

3. No terminal, execute os seguintes comandos para baixar e executar uma instância do PostgreSQL usando o Docker:

```
Copy code
docker pull postgres:latest
docker run --name etl-database -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres:latest
```
4. Conecte-se ao banco de dados PostgreSQL com o comando psql:
```
docker run -it --network=host postgres /bin/bash
psql -h SEUIP -U postgres
```
Certifique-se de substituir **SEUIP** pelo seu endereço IP. Você pode verificar o IP usando **ipconfig** (Windows) ou **ifconfig** (Linux).

5. No prompt do psql, crie um banco de dados com o nome "etl-database":

```
CREATE DATABASE "etl-database";
```
6. Para sair do prompt psql, digite:

```
\q
```

7.E, em seguida, saia do contêiner Docker:
```
\exit
```

## Executando os Scripts ETL

Agora, você pode executar os scripts **job_1.py** e **job_2.py** para realizar a extração, transformação e carregamento de dados.

## Configurando e Executando o Metabase
Para configurar e executar o Metabase, siga estas etapas:

1. Baixe a imagem mais recente do Metabase do Docker Hub:

```
docker pull metabase/metabase:latest
```

2. Execute o Metabase em um contêiner Docker:
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```
3. Agora, abra um navegador da web e acesse o Metabase digitando o seu endereço IP seguido de :3000 (a porta padrão do Metabase). Por exemplo:
```
http://SEUIP:3000
```
Você será direcionado para a interface do Metabase, onde poderá configurar fontes de dados, criar painéis e relatórios.


