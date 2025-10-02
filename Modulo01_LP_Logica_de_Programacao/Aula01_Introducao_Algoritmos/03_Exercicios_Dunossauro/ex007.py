'''
Exercício 07
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

#Calcular a área de um quadrado
lado = float(input('Digite o tamanho do lado do quadrado: '))

#Calcular o dobro dessa área
area = lado ** 2
dobro = area * 2

#Mostrar o resultado final para o usuário.
print(f'O dobro da área do quadrado é: {dobro}')