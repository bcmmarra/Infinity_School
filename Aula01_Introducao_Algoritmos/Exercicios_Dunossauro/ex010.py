'''
Exercício 10
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Formula
F = (C * 9/5) + 32
'''

c = float(input('Digite quantos graus Celsius: '))

f = (c * 9/5) + 32

print(f'{c}ºC equivale a {f} ºF')
