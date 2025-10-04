#Faça um programa que peça uma quantidade indeterminada de numeros,
# armezene-os em uma lista. Ao final mostre na tela:
# - Soma dos Números
# - Media dos Números

numeros = []

while True:
    numero = float(input('Digite um número: [0]Sair '))

    if numero == 0:
        break
    
    numeros.append(numero)

media = sum(numeros) / len(numeros)                     # Faz a média dos números da lista "len() conta quantos itens tem na lista"

print(f'A soma dos Números é: {sum(numeros)}')          # Soma todos os números da lista
print(f'A Média dos Números é: {media:.2f}')            
print(f'O maior número na lista é {max(numeros)}')      # Exibe o Maior número da da lista
print(f'O menor número na lista é {min(numeros)}')      # Exibe o Menor número da da lista

