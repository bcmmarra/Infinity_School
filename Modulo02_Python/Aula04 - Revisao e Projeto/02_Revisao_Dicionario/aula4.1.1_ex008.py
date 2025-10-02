# Faça um programa que cadastre o nome, peso e altura de 5 pessoas. Ao final, mostre todas as pessoas cadastradas e o seu IMC

# Cria uma lista vazia para armazenar os dicionários de cada pessoa
pessoas = []

# Loop para cadastrar 5 pessoas
for i in range(1):
    print(f'\n--- Cadastro da {i+1}ª pessoa ---')
    
    # Cria um dicionário vazio para a pessoa atual
    pessoa = {}
    
    # Coleta os dados e armazena no dicionário
    pessoa['nome'] = input('Nome: ')
    pessoa['peso'] = float(input('Peso (kg): '))
    pessoa['altura'] = float(input('Altura (m): '))
    
    # Calcula o IMC
    imc = pessoa['peso'] / (pessoa['altura'] ** 2)
    pessoa['imc'] = imc
    
    # Adiciona o dicionário da pessoa à lista principal
    pessoas.append(pessoa)

# Exibe todas as pessoas cadastradas
print('\n--- Pessoas Cadastradas ---')
for pessoa in pessoas:
    print(f'Nome: {pessoa["nome"]}')
    print(f'Peso: {pessoa["peso"]:.2f} kg')
    print(f'Altura: {pessoa["altura"]:.2f} m')
        
    print('-' * 20)