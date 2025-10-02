'''
🔹 Exercício 11 – Previsão de salário
Peça:

Nome do funcionário
Salário atual
Percentual de aumento (ex: 10%)

Calcule o novo salário e exiba:
João passará a ganhar R$ XXXX.XX após o aumento de 10%.
'''

nome = input("Nome do funcionário: ")
salario = float(input("Digite o Salário: R$ "))
aumento = float(input("Digite o Percentual de aumento %: "))

aumento_salario = salario + (salario * aumento/100)

print (f"{nome} pasará a ganhar R$ {aumento_salario:.2f} após o aumento de {aumento:.2f}%.")

# Resolução
nome = input("Nome do funcionário: ")
salario = float(input("Salário atual: "))
percentual = float(input("Percentual de aumento (%): "))

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"{nome} passará a ganhar R$ {novo_salario:.2f} após o aumento de {percentual}%.")

