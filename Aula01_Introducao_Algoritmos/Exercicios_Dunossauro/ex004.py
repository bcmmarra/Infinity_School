'''
Exercício 04
Faça um programa que peça as 4 notas bimestrais e mostre a média.
'''

bimestre1 = float(input('Digite a nota do 1º Bimestre: '))
bimestre2 = float(input('Digite a nota do 2º Bimestre: '))
bimestre3 = float(input('Digite a nota do 3º Bimestre: '))
bimestre4 = float(input('Digite a nota do 4º Bimestre: '))

media = (bimestre1 + bimestre2 + bimestre3 + bimestre4) / 4

print(f'A média do Aluno foi de: {media:.2f}')

