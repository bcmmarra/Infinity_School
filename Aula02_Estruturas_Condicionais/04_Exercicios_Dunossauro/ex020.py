'''Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

media = (nota1 + nota2 + nota3) / 3

if media == 10.0:
    print(f'A média foi {media:.2f}, o aluno foi APROVADO COM DISTINÇÃO')

elif media >= 7.0:
    print(f'A média foi {media:.2f}, o aluno foi APROVADO')

else:
    print(f'A média foi {media:.2f}, o aluno foi REPROVADO')