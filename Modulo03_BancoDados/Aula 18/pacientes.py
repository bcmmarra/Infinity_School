# CRUD de Paciantes
import db
from datetime import datetime, date


def listar():
    # 1. Connectar no Banco de Dados
    conn = db.get_db()

    # 2. Criar o cursor
    cursor = conn.cursor(dictionary=True)

    # 3. Buscando dados
    # 3.1 Executando Consulta
    sql = '''
        SELECT id, nome, cpf, data_nascimento, ativo
        FROM pacientes
    '''
    cursor.execute(sql)
    
    # 3.2 Trazendo dados para o python
    dados = cursor.fetchall()

    conn.close()

    return dados


def cadastrar(nome: str, cpf: str, data_nascimento: date):
    # 1. Connectar no Banco de Dados
    conn = db.get_db()

    # 2. Criar o cursor
    cursor = conn.cursor()

    # 3. Manipular o banco de dados (Executando Comandos SQL)
    sql = '''
        INSERT INTO pacientes (nome, cpf, data_nascimento)
        VALUES (%s, %s, %s)
    '''

    cursor.execute(sql, (nome, cpf, data_nascimento))
    conn.commit() # Somente para INSERT, UPDATE e DELETE

    # 4. Fechar o cursor e a conexão
    conn.close()


def atualizar():
    pass


def excluir():
    pass


def menu():
    while True:
        print('Gerenciamento de Pacientes: ')
        print('[1] - Listar')
        print('[2] - Cadastrar')
        print('[3] - Voltar')

        opcao = input('Opção: ')

        if opcao == '1':
            pacientes = listar()
            print(pacientes)
            
        elif opcao == '2':
            nome = input('Digite o nome do paciente: ')
            cpf = input('Digite o cpf do paciente: ')

            data_nascimento_str = input('Digite a data de nascimento do paciente (yyyy-mm-dd): ')
            data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()

            cadastrar(nome, cpf, data_nascimento)
            
            print('Paciente Cadastrado com Sucesso.')
        elif opcao == '3':
            break
