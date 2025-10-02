# Faça um programa para cadastrar 3 cursos que serão armazenados em um dicionário onde o nome do curso será a chave, e o valor será outro dicionário contendo "nivel" e "duração"

# Cria um dicionário vazio para armazenar todos os cursos
cursos = {}

# Usa um loop para cadastrar 3 cursos
for i in range(3):
    print(f'\n--- Cadastro do {i+1}º Curso ---')
    
    # Coleta o nome do curso para ser a chave no dicionário principal
    nome_curso = input('Digite o nome do curso: ')
    
    # Coleta as informações que ficarão no dicionário interno
    nivel = input('Digite o nível do curso (ex: Básico, Intermediário): ')
    duracao = input('Digite a duração do curso (ex: 40 horas): ')
    
    # Cria o dicionário interno com as informações do curso
    info_curso = {
        'nivel': nivel,
        'duracao': duracao
    }
    
    # Adiciona o dicionário interno ao dicionário principal, usando o nome do curso como chave
    cursos[nome_curso] = info_curso
    
print('\n--- Cursos Cadastrados ---')
print(cursos)