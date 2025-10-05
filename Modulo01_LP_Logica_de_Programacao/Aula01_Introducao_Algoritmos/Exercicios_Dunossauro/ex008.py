'''
Exercício 08
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

#Pedir o valor da hora
vlrHora = float(input('Digite o valor da hora trabalhado: R$ '))

#Pedir o número de horas
hora = float(input('Quantas horas você trabalhou neste mês? '))

#Calcular o salário
salario = vlrHora * hora

#Mostrar o resultado
print(f'O seu salário este mês é R$: {salario:.2f}')