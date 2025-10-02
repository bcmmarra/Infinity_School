'''
Exercício 09
Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

Formula
C = 5 * ((F-32) / 9).
'''

f = float(input('Digite quantos graus Fahrenheit: '))

c = 5 * ((f-32)/9)

print(f'{f}ºF equivale a {c} ºC')