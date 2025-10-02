'''
7 - "Faça um Programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c = 0. O Programa deverá pedir os valores de a, b e c e fazer as validações, informando ao usuário:"
"a. Se a = 0, a equação não é do segundo grau e o programa deve finalizar."
"b. Se o delta for negativo, a equação não possui raízes reais. Imprima esta mensagem e finalize."
"c. Se o delta for igual a zero, a equação possui apenas uma raiz real. Informe-a."
"d. Se o delta for positivo, a equação possui duas raízes reais. Informe-as."

(Lembrete: Delta = b² - 4ac; Raiz = (-b ± sqrt(Delta)) / 2a)'''
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
