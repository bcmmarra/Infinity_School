'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
- até 20 litros: desconto de 3% por litro
- acima de 20 litros: desconto de 5% por litro

Gasolina:
- até 20 litros: desconto de 4% por litro
- acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

combustivel = input('Qual combustível? A-álcool, G-gasolina: ')
litros = float(input('Digite quantos litros: '))
preco_alcool = 1.90
preco_gasolina = 2.50
preco_final = 0
desconto = 0

if combustivel == 'A':
    preco_final = preco_alcool
    if litros <= 20:
        desconto =  0.03
    else:
        desconto =  0.05

    valor_total = litros * preco_final
    valor_com_desconto = valor_total * (1 - desconto)

    # Imprime o resultado final
    print(f'O valor final a ser pago é R$ {valor_com_desconto:.2f}')
    
elif combustivel == 'G':
    preco_final = preco_gasolina
    if litros <= 20:
        desconto =  0.04
    else:
        desconto =  0.06

    valor_total = litros * preco_final
    valor_com_desconto = valor_total * (1 - desconto)

    # Imprime o resultado final
    print(f'O valor final a ser pago é R$ {valor_com_desconto:.2f}')

else:
    print("Combustivel Indisponivel.")
