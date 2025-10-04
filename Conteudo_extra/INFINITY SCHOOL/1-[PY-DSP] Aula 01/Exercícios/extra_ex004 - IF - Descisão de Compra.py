'''
4 - "Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."'''
print("---- Descisão de Compra ----")
#Pedir ao usuário o preço de três produtos.
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

#Usar a estrutura condicional para comparar os preços.
if preco1 < preco2 and preco1 < preco3:
    print(f"Você deve comprar o primeiro produto, que custa R${preco1:.2f}.")
elif preco2 < preco1 and preco2 < preco3:
    print(f"Você deve comprar o segundo produto, que custa R${preco2:.2f}.")
else:
    print(f"Você deve comprar o terceiro produto, que custa R${preco3:.2f}.")

print("---- FIM - Descisão de Compra ----")
