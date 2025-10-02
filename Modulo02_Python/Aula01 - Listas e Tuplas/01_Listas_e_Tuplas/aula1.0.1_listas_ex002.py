'''
Crie uma lista vazia chamada `nomes`.
Peça para o usuário digitar 3 nomes e adicione cada um deles à lista. Mostre a lista final.
'''

nomes=[]

print('Digite 3 nomes')

for n in range (3):
    if n < 3:
        nome = input(f'Digite o {n+1}º nome: ')
        nomes.insert(n, nome)
print(nomes)