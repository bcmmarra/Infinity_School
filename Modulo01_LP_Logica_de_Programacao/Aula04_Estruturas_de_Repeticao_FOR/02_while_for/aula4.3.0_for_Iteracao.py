'''
## Iteráveis
A estrutura do `for` na verdade utiliza o que chamamos de **iteração** para executar
a sua repetição, onde na verdade ela percorre uma sequencia de dados.
Podemos definir o verbo “iterar” como “percorrer”, onde para cada valor da sequência
ele executa o bloco do for.
Chamamos essas sequências que podem ser percorridas utilizando o `for` de **iteráveis,**
e abaixo vamos entender um pouco mais sobre os iteraveis mais básicos.
'''

### Range
# A função `range()` na verdade cria para gente uma sequencia de valores,
# observe no exemplo abaixo: interação numérica

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(3, 100, 3)))
# [3, 6, 9, 12, 15, 18, 21 ... até 99]


### Strings
# Uma string (str) nada mais é do que uma sequência de caracteres, e como qualquer uma
# sequência também é um iterável.
# Iterando uma string (str) com o for
# Exibe todas os caracteres incluindo o espaço entre as palavras.

texto = input('Digite uma palavra: ')

for letra in texto:
    print(letra)

# Contar a quantidade caracteres
texto = input('Digite uma palavra: ')
qtd_letra = 0

for letra in texto:
    if letra.lower() == 'e':
        qtd_letra += 1
    
print(f'E: {qtd_letra}')



