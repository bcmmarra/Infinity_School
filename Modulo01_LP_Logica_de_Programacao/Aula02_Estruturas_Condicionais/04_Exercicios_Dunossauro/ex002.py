'''Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')

