'''
Exercício 16
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

#Pedir o tamanho da área: O programa deve começar perguntando ao usuário qual é a área total a ser pintada, em metros quadrados. Esse valor (por exemplo, 100 m²) deve ser armazenado em uma variável.

altura = float(input('Digite o tamanho da altura da area: '))
largura = float(input('Digite o tamanho da largura da area: '))

area = altura * largura

rendimento = area / 3

lata = rendimento // 18

if lata % 18 > 0:
    lata += 1

vlr = lata * 80

print(f'A quantidade de latas que ele precisa comprar {lata}')
print(f'O Valor Total é: R$ {vlr:.2f}.')
