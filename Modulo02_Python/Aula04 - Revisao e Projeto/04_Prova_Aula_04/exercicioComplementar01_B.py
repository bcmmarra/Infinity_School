# Como ordenar uma lista numeros = [3, 1, 2]? 
# Exitem 2 metodos para ordenar os valores de uma lista:
    # 1 numeros.sort()
        # numeros.sort(): Método de lista, ordena a lista original no local, ou seja, ele altera a própria lista numeros e não retorna uma nova lista.
numeros = [3, 1, 2]
numeros.sort()
print(numeros)

# Saída: [1, 2, 3]
    # 2 sorted(numeros).
        # sorted(numeros): Função que pode ser usada em qualquer iterável (lista, tupla, etc.). Ela retorna uma nova lista ordenada e não modifica a lista original.

numeros = [3, 1, 2]
nova_lista = sorted(numeros)
print(nova_lista)
# Saída: [1, 2, 3]
print(numeros)
# Saída: [3, 1, 2] (a lista original não foi alterada)

