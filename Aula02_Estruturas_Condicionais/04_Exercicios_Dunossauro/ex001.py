'''Faça um programa que peça dois números e imprima o maior deles.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'Entre os numeros {n1} e {n2} o {n1} é maior')
elif n1 == n2:
    print(f'Os numeros {n1} e {n2} são iguais')
else:
    print(f'Entre os numeros {n1} e {n2} o {n2} é maior')