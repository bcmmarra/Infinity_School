# Soma de despesas: Peça valores de despesas até digitar um valor negativo. Mostre o total gasto.

despesa_total = 0
despesa = float(input('Digite o valor da despesa: R$ '))

while despesa >= 0:
    despesa_total += despesa
    despesa = float(input('Digite o valor da despesa: R$ '))

print(f'A sua despesa mensal foi de R$: {despesa_total}')