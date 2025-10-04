'''Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

Adicionando a logica de controle de notas disponiveis.
'''

resposta = input('Escolha uma Transação: [S]acar [X]Sair: ')

#Estoque de notas
estoque_notas2 = 30
estoque_notas5 = 50
estoque_notas10 = 10
estoque_notas20 = 8
estoque_notas50 = 5
estoque_notas100 = 2

valor_disponivel = estoque_notas2 * 1 + estoque_notas5 * 5 + estoque_notas10 * 10 + estoque_notas20 * 20 + estoque_notas50 * 50 + estoque_notas100 * 100

if valor_disponivel == 0:
    print('Saque indisponível')

else:
    while resposta.upper() != "S" and resposta.upper() != "X":
        print('Resposta inválida. Digite (S/X): ')
        resposta = input("Tente novamente. Digite: [S]acar / [X]Sair: ")
        
    while resposta.upper() == "S":    
        valor_disponivel = estoque_notas2 * 2 + estoque_notas5 * 5 + estoque_notas10 * 10 + estoque_notas20 * 20 + estoque_notas50 * 50 + estoque_notas100 * 100
        
        if valor_disponivel == 0 or valor_disponivel < 10:
            print('Saque indisponível no momento. Por favor, tente novamente mais tarde.')
            break 
        
        print('----| Notas disponivel 2, 5, 10, 20, 50 100,00 |----')
        saque = int(input('Informe o valor do saque: R$ '))

        if saque >= 2:
            if saque <= valor_disponivel:
                print(f'O valor do Saque é: {saque:.2f}')
    
                # Quantidade necessaria de notas de 100
                nota100_necessaria = saque // 100
                
                #A quantidade necessária de 100
                if nota100_necessaria <= estoque_notas100:
                    notas100 = nota100_necessaria
                    estoque_notas100 -= nota100_necessaria
                else:
                    notas100 = estoque_notas100
                    estoque_notas100 -= estoque_notas100
                
                #Resultado do restante do saque
                restante_saque = saque - (notas100 * 100)
                
                #A quantidade necessária de 50
                nota50_necessaria = restante_saque // 50
                if nota50_necessaria <= estoque_notas50:
                    notas50 = nota50_necessaria
                    estoque_notas50 -= nota50_necessaria
                else:
                    notas50 = estoque_notas50
                    estoque_notas50 -= estoque_notas50

                #Resultado do restante do saque
                restante_saque = restante_saque - (notas50 * 50)
                
                #A quantidade necessária de 20
                nota20_necessaria = restante_saque // 20
                if nota20_necessaria <= estoque_notas20:
                    notas20 = nota20_necessaria
                    estoque_notas20 -= nota20_necessaria
                else:
                    notas20 = estoque_notas20
                    estoque_notas20 -= estoque_notas20

                #Resultado do restante do saque
                restante_saque = restante_saque - (notas20 * 20)
                
                #A quantidade necessária de 10
                nota10_necessaria = restante_saque // 10
                if nota10_necessaria <= estoque_notas10:
                    notas10 = nota10_necessaria
                    estoque_notas10 -= nota10_necessaria
                else:
                    notas10 = estoque_notas10
                    estoque_notas10 -= estoque_notas10

                #Resultado do restante do saque
                restante_saque = restante_saque - (notas10 * 10)
                
                #A quantidade necessária de 5
                nota5_necessaria = restante_saque // 5
                if nota5_necessaria <= estoque_notas5:
                    notas5 = nota5_necessaria
                    estoque_notas5 -= nota5_necessaria
                else:
                    notas5 = estoque_notas5
                    estoque_notas5 -= estoque_notas5

                #Resultado do restante do saque
                restante_saque = restante_saque - (notas5 * 5)
                
                #A quantidade necessária de 2
                nota2_necessaria = restante_saque // 2
                if nota2_necessaria <= estoque_notas2:
                    notas2 = nota2_necessaria
                    estoque_notas2 -= nota2_necessaria
                else:
                    notas2 = estoque_notas2
                    estoque_notas2 -= estoque_notas2

            
                if notas100 > 1:
                    parte100 = 'notas de R$ 100,00'
                else: 
                    parte100 = 'nota de R$ 100,00'
                
                if notas50 > 1:
                    parte50 = 'notas de R$ 50,00'
                else: 
                    parte50 = 'nota de R$ 50,00'
                
                if notas20 > 1:
                    parte20 = 'notas de R$ 20,00'
                else: 
                    parte20 = 'nota de R$ 20,00'

                if notas10 > 1:
                    parte10 = 'notas de R$ 10,00'
                else: 
                    parte10 = 'nota de R$ 10,00'
                
                if notas5 > 1:
                    parte5 = 'notas de R$ 5,00'
                else: 
                    parte5 = 'nota de R$ 5,00'
                
                if notas2 > 1:
                    parte2 = 'notas de R$ 2,00'
                else: 
                    parte2 = 'nota de R$ 2,00'
                
                if notas100 >= 1:
                    print(f'{notas100} {parte100}')
                
                if notas50 >= 1:
                    print(f'{notas50} {parte50}')
                
                if notas20 >= 1:
                    print(f'{notas20} {parte20}')
                
                if notas10 >= 1:
                    print(f'{notas10} {parte10}')
                
                if notas5 >= 1:
                    print(f'{notas5} {parte5}')
                
                if notas2 >= 1:
                    print(f'{notas2} {parte2}')
            else:
                print(f'O valor do saque é superior ao disponível no caixa')
                print(f'O valor máximo disponível é R$ {valor_disponivel:.2f}')

        else:    
            print('Valor digitado fora do intervalo permitido para o saque.')
            
        resposta = input("Continuar? [S]im / Qualquer tecla para SAIR: ")    