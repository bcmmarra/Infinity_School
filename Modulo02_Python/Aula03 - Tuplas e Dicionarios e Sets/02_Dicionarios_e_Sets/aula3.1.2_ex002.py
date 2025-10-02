# Crie um dicionário para armazenar dados de pessoas, o nome será a chave e a idade o valor.

pessoas = {}
qtd_pessoas = int(input('Quantas pessoas quer adicionar: '))
for n in range(qtd_pessoas):
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    pessoas[nome] = idade
print(pessoas)
