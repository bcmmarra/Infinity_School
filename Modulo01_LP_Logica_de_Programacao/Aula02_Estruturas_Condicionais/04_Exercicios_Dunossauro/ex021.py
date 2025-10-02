'''Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input('Informe o valor do saque: R$ '))

if saque >= 10 and saque <= 600:
    print(saque)
    nota100_inteiro = saque // 100
    nota100_resto = saque % 100
    nota50_inteiro = nota100_resto // 50
    nota50_resto = nota100_resto % 50
    nota20_inteiro = nota50_resto // 20
    nota20_resto = nota50_resto % 20
    nota10_inteiro = nota20_resto // 10
    nota10_resto = nota20_resto % 10
    nota5_inteiro = nota10_resto // 5
    nota5_resto = nota10_resto % 5
    nota1_inteiro = nota5_resto // 1
    
    if nota100_inteiro > 1:
        parte100 = 'notas de R$ 100,00'
    else: 
        parte100 = 'nota de R$ 100,00'
    
    if nota50_inteiro > 1:
        parte50 = 'notas de R$ 50,00'
    else: 
        parte50 = 'nota de R$ 50,00'
    
    if nota20_inteiro > 1:
        parte20 = 'notas de R$ 20,00'
    else: 
        parte20 = 'nota de R$ 20,00'

    if nota10_inteiro > 1:
        parte10 = 'notas de R$ 10,00'
    else: 
        parte10 = 'nota de R$ 10,00'
    
    if nota5_inteiro > 1:
        parte5 = 'notas de R$ 5,00'
    else: 
        parte5 = 'nota de R$ 5,00'
    
    if nota1_inteiro > 1:
        parte1 = 'notas de R$ 1,00'
    else: 
        parte1 = 'nota de R$ 1,00'
    
    if nota100_inteiro >= 1:
        print(f'{nota100_inteiro} {parte100}')
    
    if nota50_inteiro >= 1:
        print(f'{nota50_inteiro} {parte50}')
    
    if nota20_inteiro >= 1:
        print(f'{nota20_inteiro} {parte20}')
    
    if nota10_inteiro >= 1:
        print(f'{nota10_inteiro} {parte10}')
    
    if nota5_inteiro >= 1:
        print(f'{nota5_inteiro} {parte5}')
    
    if nota1_inteiro >= 1:
        print(f'{nota1_inteiro} {parte1}')
        
else:    
    print('Valor digitado fora do intervalo permitido para o saque.')