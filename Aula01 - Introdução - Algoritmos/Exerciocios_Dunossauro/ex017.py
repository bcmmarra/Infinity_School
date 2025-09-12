'''
Exercício 17
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
altura = float(input('Digite o tamanho da altura da area: '))
print(f"Altura {altura:.2f}")
largura = float(input('Digite o tamanho da largura da area: '))
print(f"largura {largura:.2f}")

area = altura * largura
print(f"O tamanho da area é: {area:.2f} mt²")

area_com_folga = area * 1.10
print(f"O tamanho da area com 10% de margem é: {area_com_folga:.2f} mt²")

litros_necessarios = area_com_folga / 6
print(f"Quantidade necessária de litros de tinta: {litros_necessarios:.2f}L")

print('\n--- Cenário 1: Comprar Apenas Latas de 18 Litros ---')
latas = int(litros_necessarios / 18)
if litros_necessarios % 18 > 0:
    latas += 1
preco_latas = latas * 80
print(f'A quantidade de latas de 18L para compra é: {latas}')
print(f'O Valor Total das latas de 18L é: R$ {preco_latas:.2f}.')

print('\n--- Cenário 2: Comprar Apenas Galões de 3,6 Litros ---')
galoes = int(litros_necessarios / 3.6)
if litros_necessarios % 3.6 > 0:
    galoes += 1
preco_galoes = galoes * 25
print(f'A quantidade de galões de 3.6L para compra é: {galoes}')
print(f'O Valor Total dos galões de 3.6L é: R$ {preco_galoes:.2f}.')

print('\n--- Cenário 3: Misturar Latas e Galões (Otimização) ---')
latas_otimizadas = int(litros_necessarios / 18)
litros_restantes = litros_necessarios % 18
galoes_otimizados = int(litros_restantes / 3.6)
if litros_restantes % 3.6 > 0:
    galoes_otimizados += 1

preco_latas_otimizado = latas_otimizadas * 80
preco_galoes_otimizado = galoes_otimizados * 25
preco_total_otimizado = preco_latas_otimizado + preco_galoes_otimizado

print(f'A quantidade de latas para compra é: {latas_otimizadas}')
print(f'A quantidade de galões para compra é: {galoes_otimizados}')
print(f'O Valor Total (otimizado) é: R$ {preco_total_otimizado:.2f}.')