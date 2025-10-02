# [PY-A02] Crie um sistema de login que armazene usuários e senhas em um dicionário. O programa deve verificar se o usuário existe e se a senha está correta. 

# Dicionário de Usuários
usuarios = {
    'bruno': '123456',
    'camila': '654321',
    'gigi': '1234ab',
    'davi': '147852',
    'joao pedro': '963258'
}

print('--- Digite Usuário e Senha para entrar no Sistema ---')

# Entrada do usuário
usuario = input('Digite o usuários: ').lower()
senha = input('Digite a senha: ')

# Lógica de verificação se o Usuário e a Senha estão corretos.
if usuario in usuarios:
    if senha == usuarios[usuario]:
        print('Login realizado com sucesso')
    else:
        print('Usuário ou senha Incorreto')
else:
    print('Usuário ou senha Incorreto')
