'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

#Entradas
tipo_de_carne = input('Digite o tipo da carne: (F -Filé Duplo, A - Alcatra e P - Picanha: ').lower()
kg = float(input('Digite o peso em quilos: '))
forma_de_pagamento = input('Forma de Pagamento: (C - Cartão Tabajara, D - Dinheiro, P - PIX): ').lower()

#Inicialização da Váriaveis
preco_File_A = 4.90
preco_File_B = 5.80
preco_Alcatra_A = 5.90
preco_Alcatra_B = 6.80
preco_Picanha_A = 6.90
preco_Picanha_B = 7.80
cartao_tabajara = 0.05
desconto_tabajara = 0
preco = 0
preco_total = 0
valor_a_pagar = 0
cod = 0
carne = ''


#Processamento
if tipo_de_carne == "f":
    cod = '0001'
    carne = 'File Duplo'
    
    if kg <= 5:
        preco = preco_File_A
        preco_total = kg * preco_File_A
    else:
        preco = preco_File_B
        preco_total = kg * preco_File_B

elif tipo_de_carne == 'a':
    cod = '0002'
    carne = 'Alcatra PT'
    if kg <= 5:
        preco = preco_Alcatra_A
        preco_total = kg * preco_Alcatra_A
    else:
        preco = preco_Alcatra_B
        preco_total = kg * preco_Alcatra_B

elif tipo_de_carne == 'p':
    cod = '0003'
    carne = 'Picanha AR'
    if kg <= 5:
        preco = preco_Picanha_A
        preco_total = kg * preco_Picanha_A
    else:
        preco = preco_Picanha_B
        preco_total = kg * preco_Picanha_B
        
else:
    print('Opção inválida.')
    exit()


if forma_de_pagamento == "c":
    forma_de_pagamento = 'Cartão Tabajara'
    desconto_tabajara = preco_total * cartao_tabajara
    valor_a_pagar = preco_total - desconto_tabajara
else:
    forma_de_pagamento = 'Outros         '
    valor_a_pagar = preco_total
print('-'*41)
print('CNPJ: 00.000.000/0000-00 - Hipermercado TABAJARA')
print('Endereço: Avenida Python 777 - Centro - BH/MG')
print('DOCUMENTO AUXILIAR DA NOTA FISCAL DE CONSUMIDOR ELETRÔNICA')
print(f'')
print('Código    Descrição          Qtd   UN    Vl Unit     Vl Total')
print(f'{cod}      {carne}        {kg:.2f}   KG       {preco:.2f}        {kg*preco:.2f}')

print(f'\nQtde. Total de itens                                       01')
print(f'Valor Total                                          R$ {preco_total:.2f}')
print(f'Desconto Cliente Tabajara 5%:                        R$  {desconto_tabajara:.2f}')
print(f'FRETE:                                               R$  0.00')
print(f'Valor Total a Pagar:                                 R$ {valor_a_pagar:.2f}')
print(f'')
print(f'FORMA DE PAGAMENTO                                 VALOR PAGO')
print(f'{forma_de_pagamento}                                      R$ {valor_a_pagar:.2f}')
print(f'')
print(f'              CONSULTE PELA CHAVE DE ACESSO EM')
print(f'             www.fazenda.mg.gov.br/nfce/consulta')
print(f'    0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000')
print(f'')
print(f'------------- CONSUMIDOR CPF: 099.999.999-99 Avenida Python, 770')
print(f'-x    x    x- Centro - BH/MG - CEP 00.000-000')
print(f'- x   x   x -')
print(f'-  x  x  x  - NFC-e Nº 000000001  Série 001 18/08/2025')
print(f'-   x x x   - 15:03:53')
print(f'-    xxx    - Protocolo de autorização: 314 1300004001 80')
print(f'-     x     - Data da autorização: 18/08/2025 15:03:53')
print(f'-------------')
print(f'')
print(f'Tributos Totais Incidentes (Lei Federal 12.741/2012) - Total R$ 0,00')
print(f'10%Federal 40%Estadual 30%Municipal')
print(f'')
    

print('-------------FIM DO PROGRAMA-------------')
