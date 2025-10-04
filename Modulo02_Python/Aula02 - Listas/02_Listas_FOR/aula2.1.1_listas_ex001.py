# # Faça um programa que leia uma lista de 5 números inteiros e mostre-os individualmente

# print('Crie uma lista com 5 números')

# numeros =[]

# for i in range (5):
#     numero = int(input(f'Digite {i+1}º número: '))
#     numeros.append(numero)

# #Exibir os números    
# print(numeros)
# # [ X1, X2, X3, X4, Xn]

# print('Números Inseridos: ')
# for numero in numeros:
#     print(numero)
# # X1
# # X2
# # X3
# # X4
# # Xn

# #Funções úteis para listas

numeros = []

for n in range(5):
    numero = int(input(f'Digite o {n+1}º numero: '))
    numeros.append(numero)

print('Numeros Inseridos: ')
for numero in numeros:
    print(numero)

print('Soma:', sum(numeros)) # Soma de todos os números da lista ->
print('Media:', sum(numeros) / len(numeros)) # Média de todos os números da lista.

print(len(numeros))  # quantidade de elementos -> 4
print(max(numeros))  # maior valor -> 20
print(min(numeros))  # menor valor -> 5


