'''
8 - Faça um Programa que leia um número inteiro e calcule o seu fatorial.
(Lembrete: O fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. Por exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120. O fatorial de 0 é 1 (0! = 1)).'''
import math
from math import sqrt

print("---- Calcule a raiz de uma equação de segundo grau ----")
#Pedir ao usuário o horário do seu curso.
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

if a == 0:
    print(f"A equação não é de segundo grau o programa foi encerrado")
else: # Apenas se 'a' não for zero, podemos continuar
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print(f"A equação não possui raízes reais o programa foi encerrado")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"A equação possui apenas uma raíz real que é {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais que são: {raiz1} e {raiz2}")
        
print("---- FIM - Calculadora de Raízes ----")
