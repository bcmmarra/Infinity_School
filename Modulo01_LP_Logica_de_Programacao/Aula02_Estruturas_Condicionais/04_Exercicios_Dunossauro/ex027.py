'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

kg_morango = float(input('Quantos Kilos de Morango? '))
kg_maca = float(input('Quantos Kilos de Maçã? '))

tabela_A_morango = 2.50
tabela_B_morango = 2.20
tabela_A_maca = 1.80
tabela_B_maca = 1.50
desconto_Extra = 0.10
valor_desconto = 0

if kg_morango > 5:
    tabela_Morango = tabela_B_morango
    preco_Morango = kg_morango * tabela_Morango
else:
    tabela_Morango = tabela_A_morango
    preco_Morango = kg_morango * tabela_Morango
if kg_maca > 5:
    tabela_Maca = tabela_B_maca
    preco_Maca = kg_maca * tabela_Maca
else:
    tabela_Maca = tabela_A_maca
    preco_Maca = kg_maca * tabela_Maca

kg_compra = kg_morango + kg_maca
valor_compra = preco_Morango + preco_Maca

print('-'*40)
print('Lista de Produtos')
print(f'Morango:                    {kg_morango:.2f}Kg')
print(f'Maçã:                       {kg_maca:.2f}Kg')

if valor_compra > 25 or kg_compra > 8:
    valor_desconto = valor_compra * desconto_Extra
    valor_compra = valor_compra - valor_desconto
    print('-'*41)
    print('Preços:')
    print(f'Valor Total                 R$ {valor_compra:.2f}')
    print(f'Desconto Adicional 10%:     R$ {valor_desconto:.2f}')
    print(f'Valor Total com desconto:   R$ {valor_compra:.2f}')
else:
    print('-'*41)
    print('Preços:')
    print(f'Valor Total                 R$ {valor_compra:.2f}')

print('-------------FIM DO PROGRAMA-------------')
