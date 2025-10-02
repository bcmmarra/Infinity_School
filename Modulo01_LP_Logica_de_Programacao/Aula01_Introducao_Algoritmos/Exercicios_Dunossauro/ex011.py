'''
Exercício 11
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''

#Pedir os números
n1 = int(input('O primeiro número inteiro: '))
n2 = int(input('O segundo número inteiro: '))
n3 = float(input('Agora digite um número real (que pode ter casas decimais): '))

#Calcular e mostrar a primeira parte:
#Dobro do primeiro número
dobro = n1 * 2

#Metade do segundo número
metade = n2 / 2

#O produto do dobro do primeiro com metade do segundo
produto = dobro * metade

#Resultado da primeira parte
print(f'O produto do dobro do primeiro com metado do segundo é: {produto}')

#Calcular e mostrar a segunda parte:
#Triplo do primeiro número
triplo = n1 * 3

#Soma do triplo + o terceiro número
soma = triplo + n3

#Resultado da segunda parte
print(f'A soma do triplo + o terceiro número é: {soma}')

#Calcular e mostrar a terceira parte:
#O terceiro elevado ao cubo.
cubo = n3 ** 3 

#Resultado da terceira parte
print(f'O terceiro número elevado ao cubo é: {cubo}')
