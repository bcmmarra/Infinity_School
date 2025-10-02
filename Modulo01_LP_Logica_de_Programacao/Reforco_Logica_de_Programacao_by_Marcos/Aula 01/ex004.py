# Solicite três notas e informe se a média é suficiente para aprovação (média ≥ 7).

nota1 = float(input('Digite a primeiro nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print('Aluno Aprovado')
    print(f'Média: {media}')
else:
    print('Aluno Reprovado')
    print(f'Média: {media}')
