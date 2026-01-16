import db
import datetime as dt

# 1. Criar a conexão com o banco de dados
conn = db.get_db()

# 2. Criar o cursor para executar comandos SQL
cursor = conn.cursor()

# Comandos Data Manipulation Language (DML)
# SELECT - Consultar dados
# INSERT - Inserir dados
# UPDATE - Atualizar dados
# DELETE - Deletar dados

# 3. Inserir Dados
nome = input('Digite o nome do paciente: ')
cpf = input('Digite o cpf do paciente: ')

data_nascimento_str = input('Digite a data de nascimento (yyyy-mm-dd): ')
data_nascimento = dt.datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()

sql = """
    INSERT INTO pacientes (nome, cpf, data_nascimento)  
    VALUES (%s, %s, %s)
"""
cursor.execute(sql, (nome, cpf, data_nascimento))

# 4. Confirmar a transação
conn.commit()

# ?. Fechar Cursor e Conexão
cursor.close()
conn.close()
