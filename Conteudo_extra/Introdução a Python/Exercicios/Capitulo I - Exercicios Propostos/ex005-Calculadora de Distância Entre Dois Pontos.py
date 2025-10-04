'''
5. Construa um programa que tem como dados de entrada
dois pontos quaisquer no plano cartesiano: P1 e P2. Considere
que P1 é definido pelas coordenadas x1 e y1, enquanto P2 por
x2 e y2 . O programa deve calcular e escrever a distância entre
os pontos P1 e P2.

Para receber os dados de entrada, use as variáveis x1, y1, x2 e y2.
x1 = float(input(f"Digite a coordenada X1 do Ponto 1: "))
y1 = float(input(f"Digite a coordenada Y1 do Ponto 1: "))
x2 = float(input(f"Digite a coordenada X2 do Ponto 2: "))
y2 = float(input(f"Digite a coordenada Y2 do Ponto 2: "))

Dica: A função que calcula a raiz quadrada de um número real
é a sqrt (square root). Para usá-la, importe-a da biblioteca math
da seguinte forma:
import math
from math import sqrt.

A fórmula que calcula a distância entre os dois pontos é dada por:
distancia = math.sqrt(p1 + p2)

Onde:
distancia é a distância entre os dois pontos
(x1,y1) são as coordenadas do primeiro ponto
(x2,y2) são as coordenadas do segundo ponto
'''
import math
from math import sqrt

print("--- Calculadora de Distância Entre Dois Pontos ---")
print("Por favor, insira as coordenadas (x, y) de dois pontos.")

x1 = float(input(f"Digite a coordenada X1 do Ponto 1: "))
y1 = float(input(f"Digite a coordenada Y1 do Ponto 1: "))
x2 = float(input(f"Digite a coordenada X2 do Ponto 2: "))
y2 = float(input(f"Digite a coordenada Y2 do Ponto 2: "))

# --- Obter coordenadas do Ponto 1 ---
print("\n--- Coordenadas do Ponto 1 ---")
print (f"Coordenadas de X1 do Ponto 1 é: {x1}") 
print (f"Coordenadas de Y1 do Ponto 1 é: {y1}") 

# --- Obter coordenadas do Ponto 2 ---
print("\n--- Coordenadas do Ponto 2 ---")
print (f"Coordenadas de X2 do Ponto 2 é: {x2}") 
print (f"Coordenadas de Y2 do Ponto 2 é: {y2}") 

# --- Calcular a distância ---
# Diferença das coordenadas x ao quadrado
p1 = (x2 - x1)**2
# Diferença das coordenadas y ao quadrado
p2 = (y2 - y1)**2

# Soma dos quadrados e raiz quadrada
distancia = math.sqrt(p1 + p2)

# --- Exibir o resultado ---
print("\n--- Resultado ---")
print(f"Ponto 1: ({x1:.2f}, {y1:.2f})")
print(f"Ponto 2: ({x2:.2f}, {y2:.2f})")
print(f"A DISTÂNCIA entre os dois pontos é: {distancia:.2f} unidades de comprimento.")
print("-------------------------------------------------")