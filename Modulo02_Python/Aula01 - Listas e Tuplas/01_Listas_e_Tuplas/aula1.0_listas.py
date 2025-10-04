'''
## O que é uma lista?
Em Python, uma **lista** é uma estrutura que serve para **guardar vários valores dentro de uma única variável**.
📦 Pense em uma lista como uma **caixa organizadora com divisórias**:
- Cada divisória guarda um item.
- Você pode colocar itens novos, tirar, trocar de posição, e até deixar vazia.
'''
# Exemplo de lista de frutas
frutas = ["maçã", "banana", "laranja"]

#Mostra a lista inteira
print(frutas)

# Indices:  0         1         2
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])  # acessa o primeiro elemento: "maçã"
print(frutas[2])  # acessa o terceiro elemento: "laranja"

#Métodos de listas mais usados
#As listas possuem funções (métodos) prontas que ajudam a manipular os elementos.

frutas = ["maçã", "banana", "laranja"]

frutas.append("uva")         # .append(x)       = Adiciona no x final 
frutas.insert(1, "abacaxi")  # .insert(i, x)    = Adiciona "abacaxi" na posição escolhida neste caso 1
frutas[1] = "Melancia"       # frutas[x]        = Substitui o 'banana' na posição [1] por "Melancia" o índice precisa existir
frutas.pop()                 # .pop()           = Remove o último elemento
frutas.pop(0)                # .pop(0)          = Remove o elemento no índice informado


print(frutas)

#Lista com vários tipos de dados, não é indicado usar dessa forma.
pessoa = ["Bruno", 35, 1.89, True]
print(frutas)