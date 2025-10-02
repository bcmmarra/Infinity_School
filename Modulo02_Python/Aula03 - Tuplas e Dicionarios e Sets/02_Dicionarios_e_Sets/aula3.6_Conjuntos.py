## O que são conjuntos?

# São estruturas de dados que armazenam múltiplos valores.
# A grande diferença entre Dicionario e Set é que um Set não permite valores duplicados e os elementos não são ordenados.
# Um set (conjunto) é ideal quando precisamos armazenar itens únicos, sem nos preocupar com a ordem em que aparecem.

# Criando conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = set([2, 4, 6, 8])

print(conjunto1)  # {1, 2, 3, 4}
print(conjunto2)  # {8, 2, 4, 6} Repare que a ordem de exibição pode mudar — porque sets não têm índice.


# Métodos principais dos conjuntos

frutas = {"maçã", "banana", "abacaxi", "uva"}

frutas.add("laranja")       # add(x) Adiciona um elemento na ultima posição
print(f'Adicionou "banana" {frutas}')  # {'maçã', 'banana', 'abacaxi', 'uva', 'laranja'}

frutas.remove("banana")     # remove(x) Remove um elemento (erro se não existir)
print(f'Removeu "banana" {frutas}')  # {'maçã', 'laranja'}

frutas.remove("laranja")    # discard(x)    Remove se existir (não dá erro se não existir) KeyError: 'banana'
print(f'Removeu "laranja" {frutas}') # {'maçã', 'uva', 'abacaxi'}

frutas.discard("banana")    # discard(x)    Remove se existir (não dá erro se não existir) KeyError: 'banana'
print(f'Tentou remover "banana" {frutas}') # {'maçã', 'uva', 'abacaxi'}

frutas.clear()              # clear()       Remove todos os elementos
print(f'Limpou o conjunto inteiro {frutas}') # {}

# Operações entre Conjuntos

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))        # União → {1, 2, 3, 4, 5, 6}   Combina todos os elementos dos dois conjuntos em um único conjunto sem repetir valores
print(A.intersection(B)) # Interseção → {3, 4}          Retorna um novo conjunto contendo apenas os elementos que são iguais aos dois conjuntos
print(A.difference(B))   # Diferença → {1, 2}           Retorna um novo conjunto com os elementos que estão em A mas não estão em B ou vice-versa
