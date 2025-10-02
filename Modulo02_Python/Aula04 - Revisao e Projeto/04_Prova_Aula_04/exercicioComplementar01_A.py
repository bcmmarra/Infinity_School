# Qual método verifica se uma chave existe em um dicionário? 

# O operador in retorna True se a chave estiver no dicionário e False caso contrário.

alunos = {'Ana': 8.5, 'João': 7.0}

if 'Ana' in alunos:
    print('Ana está no dicionário de alunos.')

if 'Maria' not in alunos:
    print('Maria não está no dicionário de alunos.')
    
    