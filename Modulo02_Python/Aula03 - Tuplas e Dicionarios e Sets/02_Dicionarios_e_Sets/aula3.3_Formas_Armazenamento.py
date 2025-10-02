# Problema, quero armazenas N produtos
# 1º ponto: Qual é a estrutura de um produto?
# Produto = Nome, Categoria e Preço

# 1. Lista de Tuplas
produtos = [
	('Teclado', 'Eletrônico', 199.99),
	('Camisa', 'Têxtil', 39.90),
	('Sapato', 'Calçados', 149.50)
]

# 2. Lista de Dicionários
produtos = [
	{'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99},
    {'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99},
    {'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99}
]

# 3. Dicionários de Dicionários
produtos = {
    0: {'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99},
    1: {'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99},
    2: {'nome' : 'Teclado', 'Categoria' : 'Eletrônico', 'Preço' : 143.99}
}

# 4. Dicionários de Tuplas
produtos = {
    0: ('Teclado', 'Eletrônico', 199.99),
    1: ('Camisa', 'Têxtil', 39.90),
    2: ('Sapato', 'Calçados', 149.50)
}
