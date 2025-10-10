# Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def imprimir (n: int):
    for lin in range(1, n+1):
        for col in range(lin):
            print(col+1, end=' ')
        print()

n = int(input('Digite um número: '))
imprimir(n)


def piramide(n: int):
    for i in range(1, n + 1):
        for j in range(i):
            print(j+1, end=' ')
        print()

n = int(input('Digite um numero: '))
piramide(n)