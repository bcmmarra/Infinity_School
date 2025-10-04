# Controle de estoque: Peça a quantidade de produtos vendidos até digitar zero. Ao final, mostre o total vendido.


vendas = 0
qnt = int(input('Digite a quantidade de produtos vendidos: '))

while qnt > 0:
    vendas += qnt
    qnt = int(input('Digite a quantidade de produtos vendidos: '))

print(vendas)