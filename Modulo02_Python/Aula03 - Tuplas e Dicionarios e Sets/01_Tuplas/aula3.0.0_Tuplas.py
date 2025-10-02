# A principal caracteristica de uma tupla.
# Ela é definida pela , 'virgula'.
# O valor atribuido não pode ser fixo não pode ser modificado

#           0       1        2
animal = ('Café', 'Gato', 'Preto')  # Declaração completa da tupla com uso de ()
print(animal)
print(type(animal))

animal1 = 'Café', 'Gato', 'Preto'   # Declaração completa da tupla sem uso de ()
print(animal1)
print(type(animal1))

animal2 = 'Café',                   # Declaração simplificada
print(animal1)
print(type(animal1))

# animal[0] = 'Garfield' #TypeError
# não é possivel modificar o valor declarado



#           0       1        2
animal = ('Café', 'Gato', 'Preto')  # Declaração completa da tupla com uso de ()

# Desempacotamento de Tuplas
nome, especie, cor = animal
print(nome)
print(especie)
print(cor)

ponto = (10, 20)

# Desempacotamento
x, y = ponto # O indice 0 vai para a 1ª variável, o indice 1 vai para a 2ª variável
print("x =", x)  # 10
print("y =", y)  # 20


produtos = [
	('Teclado', 'Eletrônico', 199.99),
	('Camisa', 'Têxtil', 39.90),
	('Sapato', 'Calçados', 149.50)
]

produtos_filtrados = []

# Iteração Normal
for produto in produtos:
	nome, categoria, preco = produto # Podemos desempacotar dentro do for.
	print(produto) # Aqui Produto é uma Tupla, que poderiamos desempacotar.
	
# Iteração com Desempacotamento
for nome, categoria, preco in produtos:
	print(nome, categoria, preco) # Aqui já temos os dados desempacotados.

# Criar uma nova Tupla com um produto especifico: Iteração com Desempacotamento
for produto in produtos:
	nome, categoria, preco = produto    #Desempacotamento para percorrer e encontrar a categoria filtrada.
	if categoria == 'Eletrônico':
		produtos_filtrados.append(produto)
		
print(produtos_filtrados)

# Iteração com Desempacotamento
for nome, categoria, preco in produtos:
	if categoria == 'Eletrônico':
		produto = (nome, categoria, preco)
		produtos_filtrados.append(produto)
		
print(produtos_filtrados)

