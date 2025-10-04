'''
🧪 Exercício 8 – Fatura de compras
Peça:

Nome do produto
Preço unitário
Quantidade comprada

Calcule o total a pagar e imprima:
"Você comprou 3 unidades de Mouse por R$ 120.00."
'''

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o valor unitário do produto: "))
qtd = int(input("Digite a quantidade: "))

total = preco * qtd

print(f'Você comprou {qtd} unidades de {produto} por um valor unitário de R$ {preco:.2f}, o valor total a pagar é de R$ {total:.2f}.')