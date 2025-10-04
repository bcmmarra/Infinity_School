produtos = []

while True:
    print('Produtos: ')
    print(produtos)
    #Criando o Produto vazio
    produto = {}

    #Preenchendo Campos do Produto
    produto['nome'] = input('Digite o nome do produto: ')
    produto['categoria'] = input('Digite a categoria do produto: ')
    produto['preco'] = float(input('Digite o nome do produto: '))
    
    #Adicionando no banco de dados, neste caso na nossa lista de produtos
    produtos.append(produto)
    resp = input('Deseja adicionar mais um produto? [S/N]')

    if resp == "N":
        break

print(produtos)