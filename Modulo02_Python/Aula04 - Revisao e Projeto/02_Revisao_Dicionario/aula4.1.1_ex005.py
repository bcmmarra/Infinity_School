# Faça um programa que peça o nome, raça e cor de um animal e armazene as informações em um dicionário. Ao final mostre os valores nas chaves do dicionário.

# Criação do Dicionário vazio
pet = {}

# Inputs de entrada de dados para o Dicionário Sintaxe: dicionario['nome'] = nome_digitado
pet['nome'] = input('Digite o seu nome do pet: ')
pet['raca'] = input('Digite a raça do seu pet: ')
pet['cor'] = input('Digite a cor do seu pet: ')

# Exibição dos dados
print(f'O nome do seu pet é: {pet['nome']}, ele é da raça: {pet['raca']} e é da cor: {pet['cor']}')

print(pet)