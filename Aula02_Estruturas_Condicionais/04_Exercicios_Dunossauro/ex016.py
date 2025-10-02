'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
print('-'*40)
print('Equação de segundo grau')

#1. Entrada de Dados
a = float(input('Digite um número: '))

#2. Primeira Consistência: O Valor de "a" = 0;
if a == 0:
    print('O número de A é igual a 0.')
    print('Não é uma equação de 2º grau.')
else:
    b = float(input('Digite um número: '))
    c = float(input('Digite um número: '))
    
    #3. Calculando o Discriminante (Δ);
    delta = (b ** 2) - (4 * a * c)
    print(delta)
    #4. A Segunda Consistência: O Valor de Δ:

    #Se Δ for menor que 0 (Δ<0):
    if delta < 0:
        print('A equação não possui raizes reais.')
        
    elif delta == 0:
        #Se Δ for igual a 0 (Δ=0):
        denominador = 2 * a
        numerador = -b
        raiz = numerador / denominador
        print(f'A Raiz unica é {raiz}.')
    else:
        #Se Δ for maior que 0 (Δ>0):
        
        #Calcular a raiz quadrada de delta. Para isso, você pode usar delta ** 0.5.
        raiz_delta = delta ** 0.5
        
        #Calcular as duas raízes, raiz_1 e raiz_2, usando a fórmula de Bhaskara.
        #Calcular a primeira raiz (x1)

        numerador_x1 = (-1 * b) + raiz_delta
        denominador = 2 * a
        x1 = numerador_x1 / denominador

        #Calcular a primeira raiz (x2)
        numerador_x2 = (-1 * b) - raiz_delta
        x2 = numerador_x2 / denominador

        #Exibir as duas raízes para o usuário.
        print(f'A equação possui duas raízes reais e diferentes:')
        print(f'valor da Raiz 1 é {x1}')
        print(f'valor da Raiz 2 é {x2}')

print('FIM DO PROGRAMA')

