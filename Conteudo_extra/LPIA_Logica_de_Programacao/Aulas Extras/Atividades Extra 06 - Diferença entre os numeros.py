'''
🔹 Exercício 6 – Diferença entre números
Peça dois números inteiros e calcule:

A diferença absoluta entre eles (use abs())

Exemplo:
A diferença entre 30 e 50 é 20
'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
diferenca = n1 - n2

print(f"A diferença entre {n1} e {n2} é {abs(diferenca)}.")

# Resolução
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
diferenca = abs(n1 - n2)

print(f"A diferença entre {n1} e {n2} é {diferenca}")
