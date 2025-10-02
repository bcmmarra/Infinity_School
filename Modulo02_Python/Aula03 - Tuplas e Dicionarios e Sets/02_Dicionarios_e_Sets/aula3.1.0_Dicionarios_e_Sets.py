# Dados Aluno (solto)
#aluno_nome = "Bruno"
#aluno_notas = [6, 7, 8]
#aluno_media = 7.0
#aluno_esta_ativo = True

# Dicionário
aluno = {
    #chave: valor
    'nome': 'Bruno', # item
    'notas':[6, 7, 8],
    'media': 7.0,
    'ativo': True
}

# Acessando o valor de uma chave
print(aluno['nome'])
# print(aluno['nao existe']) #Quando pesquisa uma chave quando ela não existe erro: keyError

# Acessando o valor de uma chave, usando get
print(aluno.get('nome'))
# print(aluno.get('nao existe', 'Não Encontrado'))
# #Quando pesquisa uma chave usando o get caso ela não exista vai aparecer o erro: None.
# Sintaxe: print(aluno.get['chave', 'Frase para aparecer no lugar do erro None'])


# Alterar um valor
print(aluno)
aluno['nome'] = 'Camila'
print(aluno)

#Dicionário
# Exemplo de lista telefônica
telefones = {
    "Ana": "9999-1234",
    "João": "8888-4321",
    "Maria": "9777-5678"
}

print(telefones)            # Todo o discionário
print(telefones['Ana'])     # Somente o Telefone da Ana


# # Lista de Dicionários
# alunos = [
#     {
#         'nome': 'Bruno',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     },
#     {
#         'nome': 'Camila',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     },
#     {
#         'nome': 'Gigi',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     }
# ]


# # Acessando o valor de uma chave
# print(alunos[0], ['nome'])
# # print(alunos['nao existe']) #Quando pesquisa uma chave quando
# ela não existe erro: keyError

# # Acessando o valor de uma chave, usando get
# print(alunos.get['nome'])
# # print(aluno.get['nao existe', 'Não Encontrado'])
# #Quando pesquisa uma chave usando o get caso ela não exista
# vai aparecer o erro: None. Sintaxe: print(aluno.get['chave', 'Frase para aparecer no lugar do erro None'])



# Armazenar valores em um dicionário.
pet = {}

nome_pet = input('Digite o nome do seu pet: ')
especie_pet = input('Digite a espécie do pet: ')
print(nome_pet)
print(especie_pet)

# Chave é o nome_pet o valor é especie_pet
pet[nome_pet] = especie_pet
print(pet)




# Dados Aluno (solto)
aluno_nome = "Bruno"
aluno_notas = [6, 7, 8]
aluno_media = 7.0
aluno_esta_ativo = True

# Dicionário
aluno = {
    #chave: valor
    'nome': 'Bruno', # item
    'notas':[6, 7, 8],
    'media': 7.0,
    'ativo': True
}

# Acessando o valor de uma chave
print(aluno['nome'])
# print(aluno['nao existe']) #Quando pesquisa uma chave quando ela não existe erro: keyError

# Acessando o valor de uma chave, usando get
print(aluno.get('nome'))
# print(aluno.get('nao existe', 'Não Encontrado')) #Quando pesquisa uma chave usando o get caso ela não exista vai aparecer o erro: None. Sintaxe: print(aluno.get['chave', 'Frase para aparecer no lugar do erro None'])

# Alterar um valor
print(aluno)
aluno['nome'] = 'Camila'
print(aluno)


# # Lista de Dicionários
# alunos = [
#     {
#         'nome': 'Bruno',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     },
#     {
#         'nome': 'Camila',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     },
#     {
#         'nome': 'Gigi',
#         'notas':[6, 7, 8],
#         'media': 7.0,
#         'ativo': True
#     }
# ]


# # Acessando o valor de uma chave
# print(alunos[0], ['nome'])
# # print(alunos['nao existe']) #Quando pesquisa uma chave quando ela não existe erro: keyError

# # Acessando o valor de uma chave, usando get
# print(alunos.get['nome'])
# # print(aluno.get['nao existe', 'Não Encontrado']) #Quando pesquisa uma chave usando o get caso ela não exista vai aparecer o erro: None. Sintaxe: print(aluno.get['chave', 'Frase para aparecer no lugar do erro None'])