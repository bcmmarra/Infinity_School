# Crie uma lista chamada pessoas, onde cada elemento seja uma tupla
# contendo: (nome, idade).

pessoas = [
    ("Ana", 25),
    ("João", 30),
    ("Maria", 22)
]

for nome, idade in pessoas:
    print(f'{nome} tem {idade} anos')
