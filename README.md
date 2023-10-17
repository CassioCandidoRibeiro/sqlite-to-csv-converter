# File Converter: SQLite to CSV extension

## Apresentação:
Código em Python para converter tabelas 
de um arquivo .sqlite (Banco de Dados SQLite) 
em .csv (Comma Separated Values)

Eu estava estudando SQL pelo DBeaver, utilizando um Banco de Dados público da Olist, que tinha o formato SQLite.

Quando terminei o curso de SQL, fui começar o de Power BI, e eu queria utilizar o mesmo Banco de Dados para criar os Dashboards.

Mas o PowerBI não lê banco de dados com a extensão .sqlite, mas lê .csv

Então me deu a vontade de converter as tabelas de um arquivo .sqlite (Banco de Dados SQLite) em .csv (Comma Separated Values).

E ao invés de procurar um programa que fizesse isso, achei que seria muito mais legal se eu criasse um código em Python pra resolver esse problema.

## Índice:
0. Bibliotecas 
1. Carrega o arquivo .sqlite
2. Conecta no banco de dados
3. Obtém uma lista de cada tabela no banco de dados
4. Para cada tabela da lista, cria 1 arquivo .csv
4.1. Executa uma consulta SQL para selecionar os dados da tabela
4.2. Obtém as colunas da tabela
4.3. Cria um arquivo CSV e escreve as colunas como o cabeçalho
4.3.1. Escreve os dados da tabela no arquivo CSV
4.4. Printa no terminal cada arquivo convertido com sucesso
5. Fecha a conexão com o banco de dados
