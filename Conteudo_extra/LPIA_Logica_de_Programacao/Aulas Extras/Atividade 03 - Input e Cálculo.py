'''
Atividade 3 – Input e Cálculo
Peça dois números ao usuário e mostre:

A soma
A multiplicação
A média
'''

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
multiplicacao = n1 * n2
media = (n1 + n2) / 2

print(f"A soma dos números é: {soma:.2f}")
print(f"A multiplicação dos números é: {multiplicacao:.2f}")
print(f"A média dos números é: {media:.2f}")
