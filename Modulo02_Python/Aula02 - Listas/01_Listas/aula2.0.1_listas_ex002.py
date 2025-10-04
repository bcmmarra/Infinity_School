# Crie uma lista vazia chamada `nomes`.
# Peça para o usuário digitar 3 nomes e adicione cada um deles à lista. Mostre a lista final.

print('Crie uma lista com 3 nomes')

nomes = []

for i in range(3):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes.insert(i, nome)

print(nomes)
