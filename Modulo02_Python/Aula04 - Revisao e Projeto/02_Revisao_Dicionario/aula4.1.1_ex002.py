# Ex02. Faça um programa que peça o nome e o preço de um produto, armazene essas informações em um dicionário, nas chaves 'nome' e 'preco' respectivamente.

produto = {}

produto['nome'] = input('Digite um produto: ')
produto['preco'] = float(input('Digite o valor do produto: R$ '))

print(produto)

