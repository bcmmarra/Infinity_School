'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

usuario = input('Crie um Usuário: ')
senha = input('Crie uma senha: ')

while senha.lower() == usuario.lower():
    print('Senha não pode ser igual ao usuario')
    senha = input('Crie uma senha: ')
    
print('Senha criada com sucesso...')