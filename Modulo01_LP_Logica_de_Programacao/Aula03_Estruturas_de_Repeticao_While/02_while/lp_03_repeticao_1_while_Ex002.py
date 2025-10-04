'''Faça um programa que peça um numero positivo para o usuário, e realize uma contagem de 1 até esse numero (ele incluso).'''

num = int(input('Digite um número positivo: '))
contador = 0

while contador < num:
    contador += 1
    print(contador)

print('Fim')