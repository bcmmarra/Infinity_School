import db

# 1. Criar a conexão com o banco de dados
conn = db.get_db()

# 2. Criar o cursor para executar comandos SQL
cursor = conn.cursor(dictionary=True)

# 3. Buscando Dados
# 3.1 Selecionar todos os pacientes
sql = """
    SELECT
    id,
    nome,
    cpf,
    data_nascimento
    FROM pacientes
"""
cursor.execute(sql)

# 3.2 Trazendo dados para o python
pacientes = cursor.fetchall()

# 4. Fechar Cursor e Conexão
cursor.close()
conn.close()