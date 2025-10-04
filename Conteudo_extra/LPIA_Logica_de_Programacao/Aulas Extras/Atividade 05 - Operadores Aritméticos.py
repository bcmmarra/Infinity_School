'''
Atividade 5 – Operadores Aritméticos
Use dois números definidos e exiba os resultados de:
+, -, *, /, //, %, **
'''

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print(f"A soma de {n1} e {n2} é: {n1 + n2:.2f}")
print(f"A subtração de {n1} e {n2} é: {n1 - n2:.2f}")
print(f"A multiplicação de {n1} e {n2} é: {n1 * n2:.2f}")
print(f"A divisão de {n1} e {n2} é: {n1 / n2:.2f}")
print(f"A divisão inteira de {n1} e {n2} é: {n1 // n2:.2f}")
print(f"O resto da divisão de {n1} e {n2} é: {n1 % n2:.2f}")
print(f"A potência de {n1} e {n2} é: {n1 ** n2:.2f}")