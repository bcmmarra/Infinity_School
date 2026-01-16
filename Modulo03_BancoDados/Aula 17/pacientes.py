import db
from datetime import date
from typing import TypedDict

class Paciente(TypedDict):
    id: int
    nome: str
    cpf: str
    data_nascimento: date
    ativo: int

def listar_pacientes() -> list[Paciente]:    
    # 1. Criar a conexão com o banco de dados
    conn = db.get_db()

    # 2. Criar o cursor para executar comandos SQL
    cursor = conn.cursor(dictionary=True)

    # 3. Consultar Dados
    sql = "SELECT id, nome, cpf, data_nascimento, ativo FROM pacientes"
    cursor.execute(sql)

    # 4. Recuperar os dados
    pacientes = cursor.fetchall()

    # 5. Fechar Cursor e Conexão
    cursor.close()
    conn.close()
    
    return pacientes


def adicionar_paciente(nome, cpf, data_nascimento):
    # 1. Criar a conexão com o banco de dados
    conn = db.get_db()

    # 2. Criar o cursor para executar comandos SQL
    cursor = conn.cursor()

    # 3. Inserir Dados
    sql = """
        INSERT INTO pacientes (nome, cpf, data_nascimento)  
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (nome, cpf, data_nascimento))

    # 4. Confirmar a transação
    conn.commit()

    # 5. Fechar Cursor e Conexão
    cursor.close()
    conn.close()

    
