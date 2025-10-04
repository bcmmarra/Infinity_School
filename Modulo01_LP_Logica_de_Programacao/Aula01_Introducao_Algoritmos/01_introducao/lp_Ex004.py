'''
Atividade - 04
Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética.
Exemplo de Saída:
Digite a 1ª nota: 5.0
Digite a 2ª nota: 5.0
Digite a 3ª nota: 7.0
Digite a 4ª nota: 7.0
Média: 6.0
'''
bimestre1 = int(input("Digite a nota do 1º Bimestre: "))
bimestre2 = int(input("Digite a nota do 1º Bimestre: "))
bimestre3 = int(input("Digite a nota do 1º Bimestre: "))
bimestre4 = int(input("Digite a nota do 1º Bimestre: "))

media = (bimestre2 + bimestre2 + bimestre3 + bimestre4) / 4

print(f"O resultado da média é: {media}")
