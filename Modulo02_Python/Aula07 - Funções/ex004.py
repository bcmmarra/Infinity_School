# Faça funções para contar vogais:

# a. Faça uma função "contar_vogais" que recebe um parametro "texto" que é do tipo string e retorna a quantidade de vogais no texto e retorna um inteiro (a quantidade total de vogais)

# Exemplo:
# contar_vogais('Amor') # 2
# contar_vogais('Amora') # 3

# b. Melhore a função anterior, para retornar um dicionário ao invés de um inteiro, onde as chaves são as vogais e o valor é a quantidade, 

# Exemplo:
# contar_vogais('Amor') # {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 0}
# contar_vogais('Ultra Man') # {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 1}

# A
def contar_vogais (palavra: str) -> int:
    qtd_vogais = 0
    for letra in palavra.lower():
        if letra.lower() in 'aeiou':
             qtd_vogais += 1       
    return qtd_vogais

palavra = input('Digite uma palavra:')
qtd_vogais = contar_vogais(palavra)
print(f'A palavra {palavra} tem {qtd_vogais} vogais no total.')

# B
def dic_vogais (palavra: str) -> dict[str, int]:
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palavra.lower():
        if letra in 'aeiou':
            vogais[letra] += 1
    return vogais

palavra = input('Digite uma palavra:')
dicionario = dic_vogais(palavra)

print(dicionario)


