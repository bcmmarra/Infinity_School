'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

pergunta1 = input('Telefonou para a vítima? (nao / sim): ').lower()
pergunta2 = input('Esteve no local do crime? (nao / sim): ').lower()
pergunta3 = input('Mora perto da vítima? (nao / sim): ').lower()
pergunta4 = input('Devia para a vítima? (nao / sim): ').lower()
pergunta5 = input('Já trabalhou com a vítima? (nao / sim): ').lower()

sim = 0

if pergunta1 == 'sim':
    sim += 1

if pergunta2 == 'sim':
    sim += 1

if pergunta3 == 'sim':
    sim += 1

if pergunta4 == 'sim':
    sim += 1

if pergunta5 == 'sim':
    sim += 1

if sim == 2:
    print('Você é um SUSPEITO')
elif sim == 3 or sim == 4:
    print('Você é um CÚMPLICE')
elif sim == 5:
    print('Você é o ASSASSINO')
else:
    print('Você é INOCENTE')
    