'''Faça um programa que leia três números e mostre o maior deles:'''

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    print(f'Entre os numeros {n1}, {n2} e {n3} o {n1} é maior')
elif n2 > n1 and n2 > n3:
    print(f'Entre os numeros {n1}, {n2} e {n3} o {n2} é maior')
else:
    print(f'Entre os numeros {n1}, {n2} e {n3} o {n3} é maior')