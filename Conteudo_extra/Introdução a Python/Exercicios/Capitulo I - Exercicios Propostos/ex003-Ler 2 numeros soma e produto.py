'''
3. Construa um programa que leia 2 números reais informados
pelo usuário. Ao fim, o programa deve calcular e imprimir:
a. A soma dos dois valores
b. O produto entre eles. #--- O "Produto" é o nome dado ao resultado de uma operação de multiplicação.
'''

print("--- Programa para Ler 2 números reais ---")

n1 = float(input("Digite um número real: "))
n2 = float(input("Digite um número real: "))

soma = n1 + n2
produto = n1 * n2

print(f"O primeiro número foi: {n1:.2f}")
print(f"O segundo número foi: {n2:.2f}")
print(f"O resultado da soma de n1 e n2 é: {soma:.2f}")
print(f"O resultado do produto de n1 e n2 é: {produto:.2f}")