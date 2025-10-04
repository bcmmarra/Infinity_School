'''
Você é um operador de caixa em um supermercado e precisa implementar um programa para registrar as compras dos clientes. O programa deve solicitar o nome e o preço de cada produto e somar o total da compra no final. O operador pode inserir o nome e o preço de cada produto repetidamente até que ele deseje encerrar a compra, digitando um valor especial (por exemplo, -1). Utilize o laço de repetição while para permitir a inserção contínua dos preços dos produtos até que o operador decida encerrar a compra
'''
print("---- Lista de Compras ----")

produto = ""
total = 0

while produto != "x":
    print("Digite x para encerrar")
    produto = input("Digite o produto: ")
    produto = produto.lower()
    if produto != "x":
        preco = float(input("Digite o valor: "))
        total += preco
        print("-" * 20)

print("-" * 20)
print(f"O valor total da compra é: R${total:.2f}")

print("---- FIM - Lista de Compras ----")