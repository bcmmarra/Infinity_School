'''
Crie uma lista com 5 cidades do Brasil.
Depois, mostre na tela apenas a primeira e a última cidade.
'''

cidades = ['Sete Quedas', 'Esmeraldas', 'Belo Horizonte', 'Foz do Iguaçu', 'Cascavel']

print(f'Cidades: {cidades[0]} e {cidades[4]}')

print(cidades[len(cidades)-1])  # Acessar o último elemento quando eu não sei quantos elementos tem na lista
print(cidades[-1])              # Forma simplificada para acessar o último elemento quando eu não sei quantos elementos tem na lista

print(f'Cidades: {cidades[0]} e {cidades[-1]}')
