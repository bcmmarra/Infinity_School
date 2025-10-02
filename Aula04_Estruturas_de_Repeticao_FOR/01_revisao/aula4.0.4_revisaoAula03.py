''' Faça um programa que peça uma quantidade de números para o usuário e ao final mostre a média de todos os números
'''

soma = 0
contador = 0

qtd_numeros = int(input('Quantos número você quer somar a média? '))

while contador < qtd_numeros:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1

media = soma / qtd_numeros

print(f"Foi somado {qtd_numeros} números, a soma total foi de: {soma} e a média é {media:.2f}. ")

print('Fim do programa')

