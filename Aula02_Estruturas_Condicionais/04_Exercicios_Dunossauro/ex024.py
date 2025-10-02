'''Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''


num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))

operador = input('Digite um operador matemático: (+, -, *, /): ')

if operador =='+' or operador =='-' or operador =='*' or operador =='/':

    if operador == '+':
        numero = num1 + num2
        print(f'O Resultado da Operação: {num1:.2f} + {num2:.2f} = {numero:.2f}')
    elif operador == '-':
        numero = num1 - num2
        print(f'O Resultado da Operação: {num1:.2f} - {num2:.2f} = {numero:.2f}')
    elif operador == '*':
        numero = num1 * num2
        print(f'O Resultado da Operação: {num1:.2f} * {num2:.2f} = {numero:.2f}')
    elif operador == '/':
        numero = num1 / num2
        print(f'O Resultado da Operação: {num1:.2f} / {num2:.2f} = {numero:.2f}')

    if  (numero % 2) == 0:
        print('O resultado da Operação realizada é um número PAR')
    else:
        print('O resultado da Operação realizada é um número ÍMPAR')
        
    if numero < 0:
        print('O resultado da Operação realizada é um número NEGATIVO')
    else:
        print('O resultado da Operação realizada é um número POSITIVO')

    if numero == int(numero):
        print('O resultado da Operação realizada é um número INTEIRO')
    else:
        print('O resultado da Operação realizada é um número DECIMAL')

else:
    print('Operador selecionado INVÁLIDO')
