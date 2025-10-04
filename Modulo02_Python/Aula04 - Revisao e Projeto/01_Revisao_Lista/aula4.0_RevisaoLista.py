
nomes = []

while True:
    nome = input('Digite um nome [N] sair: ')

    if nome.upper() == 'N':
        break

    nomes.append(nome)

print(nomes)

print("-" * 30)
print('Nomes Adicionados: ')

for nome in nomes:
    print(nome)