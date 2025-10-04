# Desafio!
# Faça um programa de calculadora utilizando funções!
# O seu programa deverá iniciar e perguntar ao usuário qual operação ele deseja realizar: `somar`, `subtrair`, `multiplicar` ou `dividir`
# Cada uma das opções deverá ser ter uma função para realizar as operações matemáticas.


print('-'*30)
print('Calculadora')
print('-'*30)

# Função
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2


num1 = float(input('Numero: '))
operacao = input('[+]Somar [-]subtrair [*]multiplicar [/]Dividir? ')
num2 = float(input('Numero: '))

if operacao == '+':
    res = somar(num1, num2)
    print(f'{res:.2f}')
elif operacao == '-':
    res = subtrair(num1, num2)
    print(f'{res:.2f}')
elif operacao == '*':
    res = multiplicar(num1, num2)
    print(f'{res:.2f}')
elif operacao == '/':
    res = dividir(num1, num2)
    print(f'{res:.2f}')
else:
    print('Operador inválido...')