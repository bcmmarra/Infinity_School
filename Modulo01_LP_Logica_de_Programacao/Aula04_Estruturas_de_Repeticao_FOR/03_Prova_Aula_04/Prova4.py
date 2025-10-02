'''
[LP-A04] Exercício de Loops: Verificação de Multas por Atraso de Pagamento

O advogado precisa verificar se a empresa de um cliente está atrasando o pagamento de salários. Ele vai calcular o número de dias em atraso e, se o atraso for superior a 5 dias, será aplicada uma multa de 2% ao valor do salário por dia de atraso.

Desafio:
O código deve perguntar o valor do salário e o número de dias de atraso no pagamento. Caso o número de dias de atraso seja superior a 5, a multa será de 2% ao dia sobre o valor do salário.
Perguntar o valor do salário.
Perguntar o número de dias de atraso.
Calcular a multa, caso o atraso seja superior a 5 dias, e exibir o valor total da multa.

Exemplo:
Salário: R$ 2.000,00
Dias de atraso: 7
Multa diária: 2% do salário por dia.
'''

print(f'CALCULADORA DE MULTA POR ATRASO DE PAGAMENTO')

resposta = input("Iniciar?: [S]im / [N]ão: ")

while resposta.upper() != "S" and resposta.upper() != "N":
    print('Resposta inválida. Digite (S/N): ')
    resposta = input("Tente novamente. Digite: [S]im / [N]ão: ")

while resposta.upper() == "S":
    salario = float(input('Digite o SALÁRIO: R$ '))
    dias_atraso = int(input('Quantos dias de atraso? '))
    if dias_atraso > 5:
        percentual_multa = 0.02
        valor_multa = salario * percentual_multa
        multa = dias_atraso * valor_multa
        print(f'Salário: R$ {salario:.2f}')
        print(f'Dias de atraso: {dias_atraso}')
        print(f'Multa diária: 2% do salário por dia, valor da multa a pagar: R$ {multa:.2f}')
        print(f'Valor a ser pago ao funcionário é R$ {salario + multa:.2f}')
    else:
        print('Pagamento feito dentro do periodo permitido.')
    
    resposta = input("Continuar? [S]im / Qualquer tecla para SAIR: ")    

print(f'FIM DO PROGRAMA')
