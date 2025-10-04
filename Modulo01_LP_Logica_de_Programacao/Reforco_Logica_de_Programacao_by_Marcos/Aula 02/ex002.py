# Crie uma lista de nomes e pergunte se quer adicionar outro nome se não sai da lista e mostra a lista completa 


nomes = ['Bruno', 'Camila', 'Gigi', 'Davi', 'João']

print(f'Os nomes da lista são: {nomes}')

while True:
    resp = input('Deseja adicionar outro nome? [S]Sim | [N]Não: ')

    if resp.lower() == 's':
        nome = input('Digite outro NOME: ')
        nomes.append(nome)
    else:
        break
    
print(nomes)

