'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))

media = (n1 + n2) / 2

if media == 10:
    print(f'A média foi: {media:.2f} ')
    print(f'Aluno foi Aprovado com Distinção')
elif media >= 7:
    print(f'A média foi: {media:.2f} ')
    print(f'Aluno foi Aprovado')
else:
    print(f'A média foi: {media:.2f} ')
    print(f'Aluno foi Reprovado')