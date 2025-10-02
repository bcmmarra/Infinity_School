'''Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = input('Digite F - Feminino ou M - Masculino: ')

if sexo == "F" or sexo == "f":
    print(f'Você é do Sexo Feminino')
elif sexo == "M" or sexo == "m":
    print(f'Você é do Sexo Masculino')
else:
    print(f'Opção Inválida')
    