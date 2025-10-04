'''Exercício 2:
"Faça um Programa que peça ao usuário um valor e mostre na tela se o valor é positivo ou negativo."'''
#Pedir número ao usuário.
num1 = float(input("Digite um número: "))

#Usar a estrutura condicional para verificar se o número é positivo ou negativo.
if num1 < 0:
    print(f"O número {num1} é NEGATIVO")
elif num1 == 0:
    print(f"O número {num1} é igual a 0")
else:
    print(f"O número {num1} é POSITIVO")