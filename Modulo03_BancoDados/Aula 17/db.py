# SQL com Python

# Criando um ambiente virtual
# python -m venv .venv

# Ativando o ambiente virtual no Windows
# .venv\Scripts\activate
# Se der erro na ativação, rode o comando no windows powershell (CMD): Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Instalação do conector MySQL
# pip install mysql-connector-python

# Importando o conector MySQL
import mysql.connector as mysql

# Credenciais de Banco de Dados
# NÃO FICAM NO CÓDIGO FONTE!!!
# Utilizar variáveis de ambiente ou arquivos de configuração

# Conectando ao banco de dados
def get_db():
    conn = mysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='in12345678',
        db='hospital'
    )

    return conn

