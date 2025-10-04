'''
2 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
print("---- Ordem decrescente ----")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifique qual número é o maior primeiro
if num1 >= num2 and num1 >= num3:
    # Se num1 é o maior, agora compare num2 e num3 para o segundo e terceiro lugar
    maior = num1
    if num2 >= num3: # Se num2 for maior ou igual a num3
        meio = num2
        menor = num3
    else: # Se num3 for maior que num2
        meio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    # Se num2 é o maior, agora compare num1 e num3 para o segundo e terceiro lugar
    maior = num2
    if num1 >= num3: # Se num1 for maior ou igual a num3
        meio = num1
        menor = num3
    else: # Se num3 for maior que num1
        meio = num3
        menor = num1
else:
    # Se num3 é o maior, agora compare num1 e num2 para o segundo e terceiro lugar
    maior = num3
    if num1 >= num2: # Se num1 for maior ou igual a num2
        meio = num1
        menor = num2
    else: # Se num2 for maior que num1
        meio = num2
        menor = num1
print(f"Os números em ordem decrescente são: {maior}, {meio}, {menor}")
print("---- FIM - Ordem decrescente ----")
