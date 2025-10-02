'''
🔹 Exercício 8 – Produto total de estoque
Peça:

Nome do produto
Quantidade em estoque
Preço por unidade

Calcule o valor total do estoque.
'''

produto = input("Digite um Produto: ")
estoque = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: R$ "))

print (f"{estoque} unidade(s) do {produto} com o valor total do estoque de R$ {estoque * preco:.2f}.")

# Resolução
produto = input("Produto: ")
quantidade = int(input("Quantidade em estoque: "))
preco = float(input("Preço unitário: "))

total = quantidade * preco
print(f"Estoque de {produto}: R$ {total:.2f}")
