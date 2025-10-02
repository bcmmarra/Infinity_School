'''
Exercício 15
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
#Pedir o valor da hora
vlrHora = float(input('Digite o valor da hora trabalhado: R$ '))

#Pedir o número de horas
hora = float(input('Quantas horas você trabalhou neste mês? '))

#Calcular o salário
salarioBruto = vlrHora * hora
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

descontos = ir + inss + sindicato

salarioLiquido = salarioBruto - descontos

#Mostrar o resultado
print(f'O seu salário este mês é:')
print(f'+ Salário Bruto : R$ {salarioBruto:.2f}')
print(f'- IR (11%) : R$ {ir:.2f}')
print(f'- INSS (8%) : R$ {inss:.2f}')
print(f'- Sindicato ( 5%) : R$ {sindicato:.2f}')
print(f'= Salário Liquido : R$ {salarioLiquido:.2f}')