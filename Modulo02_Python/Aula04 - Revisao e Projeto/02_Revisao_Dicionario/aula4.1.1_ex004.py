# Faça um programa que peça as informações de uma pessoa (nome, altura e idade) e armazene em um dicionário, ao final mostre as informações dessa pessoa.

# Criação do Dicionário vazio
pessoa = {}

# Inputs de entrada de dados para o Dicionário Sintaxe: dicionario['nome'] = nome_digitado
pessoa['nome'] = input('Digite o seu nome: ')
pessoa['altura'] = float(input('Digite a sua altura: '))
pessoa['idade'] = int(input('Digite a sua idade: '))

# Exibição dos dados
print(f'O seu nome é: {pessoa['nome']}, você tem {pessoa['altura']}mts de altura e tem {pessoa['idade']} anos.')

