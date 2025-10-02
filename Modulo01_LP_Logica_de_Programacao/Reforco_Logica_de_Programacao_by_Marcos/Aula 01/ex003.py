# Peça um número e diga se é par ou ímpar.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'Número: {numero} é PAR')
else:
    print(f'Número: {numero} é IMPAR')