'''Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de dois lados for maior que o terceiro;
Se pelo menos uma dessas três condições for falsa, os valores não podem formar um triângulo. Seu programa deve verificar as três e, se todas forem verdadeiras, você pode seguir para a próxima etapa. Caso contrário, você já deve informar ao usuário que os valores não formam um triângulo.

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado1 = float(input('Digite o comprimento do 1º lado do triângulo: '))
lado2 = float(input('Digite o comprimento do 2º lado do triângulo: '))
lado3 = float(input('Digite o comprimento do 3º lado do triângulo: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('Os tamanhos fornecidos forma um Triângulo do tipo:')
    if lado1 == lado2 == lado3:
        print('Triangulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triangulo Isósceles')
    elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3:
        print('Triangulo Escaleno')
else:
    print('Não é possivel formar um Triângulo com os tamanhos fornecidos.')

