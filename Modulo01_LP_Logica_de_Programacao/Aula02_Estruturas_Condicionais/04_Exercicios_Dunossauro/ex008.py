'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
'''

produto1 = float(input('Digite o valor do 1º Produto: R$ '))
produto2 = float(input('Digite o valor do 2º Produto: R$ '))
produto3 = float(input('Digite o valor do 3º Produto: R$ '))

if produto1 < produto2 and produto1 < produto3:
    print(f"Comprar o Produto 1 que custa R$ {produto1:.2f}")
elif produto2 < produto3:
    print(f"Comprar o Produto 2 que custa R$ {produto2:.2f}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"Comprar o Produto 3 que custa R$ {produto3:.2f}")
else:
    print(f"Comprar qualquer um dos Produtos pois todos custam o mesmo valor R$ {produto1:.2f}")