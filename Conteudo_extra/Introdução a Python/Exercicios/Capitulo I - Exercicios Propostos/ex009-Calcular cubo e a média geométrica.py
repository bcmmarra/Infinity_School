'''
9. Construa um programa que solicite que o usuário informe 2 números inteiros positivos. O programa deve calcular:
a) O cubo do segundo número
num2 ** 3 realiza o cálculo do cubo de forma direta.

b) A média geométrica entre o primeiro e o segundo número.
isto é:

media_geo= sqrt[2](num_1)times(num_2)
'''
import math

print("--- Calcular cubo e a média geométrica ---")

# --- Obter os valores ---
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

cubo = num2 ** 3
'''
Cálculo da Média Geométrica:
Primeiro, calcula o produto dos dois números.
Em seguida, usa math.sqrt() para encontrar a raiz quadrada desse produto, que é a média geométrica.
O resultado é formatado para duas casas decimais (:.2f) para uma exibição limpa.
'''
media_geo= math.sqrt(num1*num2)

# --- Exibir os resultados ---
print(f"\na) O cubo do segundo número ({num2}) é: {cubo}")
print(f"b) A média geométrica entre {num1} e {num2} é: {media_geo:.2f}")
print("------------------------------------------")