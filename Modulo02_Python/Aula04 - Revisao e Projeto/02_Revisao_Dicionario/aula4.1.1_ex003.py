# Ex03. Faça um programa que peça o nome e o preço de 3 produtos, armazene as informações de cada produto em um dicionário, nas chaves 'nome' e 'preco', e cada dicionário deve ser armazenado em uma lista, formando a estrutura abaixo:
'''python
# Lista no Inicio.
produtos = []

# Lista no Final (Pode ser qualquer produto).
produtos = [
    # Exemplo de um produto
    {
        'nome': 'Teclado',
        'preco': 34.5
    },
    {
        'nome': 'Mouse',
        'preco': 44.5
    },
    # Outros Produtos
]'''

produtos = []

for n in range(3):
    produto = {}
    produto['nome'] = input('Digite um produto: ')
    produto['preco'] = float(input('Digite o valor do produto: R$ '))
    produtos.append(produto)

print(produtos)
