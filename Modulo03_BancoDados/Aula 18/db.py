# Arquivo de Conexão do Banco de Dados

import mysql.connector as mysql

def get_db():
    conn = mysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='in12345678',
        db='hospital'
    )

    return conn