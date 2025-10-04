nomes = ['Bruno', 'Camila', 'Gigi', 'Davi', 'João']


for nome in nomes:
    print(f'Os nomes da lista são: {nomes}')

    if nomes:
        print(f'Adultos {nomes[0], nomes[1]}')

for b in range(len(nomes)):
    print(f'{b+1} {nomes[b]}')

for posicao, c in enumerate(nomes, 1):
    print(f'A posição é {posicao} do nome {c}')

