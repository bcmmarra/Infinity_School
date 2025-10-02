# Faça uma lista onde vai ser verificada as contas com valor maior que 200 reais para cima 

valores = []
maior = []

while True:
    valor = float(input('Digite o valor da despesa: [0]Sair '))

    if valor == 0:
        break
    elif valor > 200:
        maior.append(valor)
        valores.append(valor)
    else:
        valores.append(valor)
print()

for valor in valores:
    print(f'Os valores digitados são: {valor:.2f} ')
print()

for valor in maior:
    print(f'Valor maior que 200: {valor:.2f} ')
