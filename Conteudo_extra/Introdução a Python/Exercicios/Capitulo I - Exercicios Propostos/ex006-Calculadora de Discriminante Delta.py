'''
6. Considere uma equação do segundo grau, representada pela expressão ax²+bx+c=0.

Construa um programa no qual o usuário informe os valores das constantes a, b e c.
Ao fim, o programa deve calcular e imprimir o valor de DELTA.
Sabe-se que Δ = b2-4ac.
'''

print("--- Calculadora de Discriminante (Delta) ---")
print("Para a equação ax² + bx + c = 0")
print("Por favor, digite os valores dos coeficientes a, b e c.")

# --- Função para obter um coeficiente e validar a entrada ---
# --- Obter os coeficientes ---
a = float(input(f"Digite valor de a: "))
b = float(input(f"Digite valor de b: "))
c = float(input(f"Digite valor de c: "))

# --- Calcular o discriminante (Delta) ---
# Fórmula: Delta (Δ) = b² - 4ac
delta = (b**2) - (4 * a * c)
# --- Exibir os coeficientes e o resultado do Delta ---
print("\n--- Coeficientes Informados ---")
print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")

print("\n--- Resultado do Discriminante (Delta) ---")
print(f"Δ = b² - 4ac")
print(f"Δ = ({b:.2f})² - 4 * ({a:.2f}) * ({c:.2f})")
print(f"O valor de Delta (Δ) é: {delta:.2f}")
print("------------------------------------------")