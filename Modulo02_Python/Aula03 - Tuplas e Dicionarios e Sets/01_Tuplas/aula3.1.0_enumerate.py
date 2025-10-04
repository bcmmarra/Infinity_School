## Enumerações
# O python tem uma função chamada enumerate que permite criar uma lista de tuplas a partir de um iteravel qualquer.

nomes = ['Davi', 'Fernanda', 'Margot']
print(list(enumerate(nomes))) # [(0, 'Davi'), (1, 'Fernanda'), (2, 'Margot')]
# O enumerate cria uma enumeração para cada valor do iteravel, começando de 0 e de forma respectiva.

# Podemos utilizar essa enumeração para poder percorrer, desempacotando:
# Lista
nomes = ['Davi', 'Fernanda', 'Margot']

# Percorrendo Enumeração
# O valor da enumeração vai para o 1º valor, e o valor da lista vai para o 2º
for index, nome in enumerate(nomes):
	print(f'[{index}] - {nome}')