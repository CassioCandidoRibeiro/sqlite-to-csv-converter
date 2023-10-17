# sqlite-to-csv-converter
# File Converter: SQLite to CSV extension

# Apresentação:
# Código em Python para converter tabelas 
# de um arquivo .sqlite (Banco de Dados SQLite) 
# em .csv (Comma Separated Values)

# Índice:
# 0. Bibliotecas 
# 1. Carrega o arquivo .sqlite
# 2. Conecta no banco de dados
# 3. Obtém uma lista de cada tabela no banco de dados
# 4. Para cada tabela da lista, cria 1 arquivo .csv
# 4.1. Executa uma consulta SQL para selecionar os dados da tabela
# 4.2. Obtém as colunas da tabela
# 4.3. Cria um arquivo CSV e escreve as colunas como o cabeçalho
# 4.3.1. Escreve os dados da tabela no arquivo CSV
# 4.4 Printa no terminal cada arquivo convertido com sucesso
# 5. Fecha a conexão com o banco de dados

# 0. Bibliotecas
import sqlite3
import csv

# 1. Carrega o arquivo .sqlite
sqlite_file = 'db_olist.sqlite'

# 2. Conecta no banco de dados
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

# 3. Obtém uma lista de cada tabela no banco de dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 4. Para cada tabela da lista, cria 1 arquivo .csv
for table in tables:
    table_name = table[0]
    csv_file = f'{table_name}.csv'

    # 4.1. Executa uma consulta SQL para selecionar os dados da tabela
    cursor.execute(f"SELECT * FROM {table_name}")

    # 4.2. Obtém as colunas da tabela
    columns = [description[0] for description in cursor.description]

    # 4.3. Cria um arquivo CSV e escreve as colunas como o cabeçalho
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

        # 4.3.1. Escreve os dados da tabela no arquivo CSV
        for row in cursor:
            writer.writerow(row)

    # 4.4 Printa no terminal cada arquivo convertido com sucesso
    print(f'O arquivo CSV {csv_file} foi criado com sucesso.')

# 5. Fecha a conexão com o banco de dados
connection.close()

