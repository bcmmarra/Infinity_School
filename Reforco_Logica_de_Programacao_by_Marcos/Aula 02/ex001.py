#Crie uma  lista de nomes e coloque nomes dentro dela, para cada nome mostra a posição que ele esta. 

nomes = ['Bruno', 'Camila', 'Gigi', 'Davi', 'João']


print(f'Os nomes da lista são: {nomes}')

for posicao in range(len(nomes)):
    print(f'A posição é {posicao+1} do nome: {nomes[posicao]}')
    