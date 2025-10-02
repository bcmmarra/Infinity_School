print('---- APROVADO, EM RECUPERAÇÃO ou REPROVADO? ----')

nota1 = float(input('Digita a 1ª Nota: '))
nota2 = float(input('Digita a 2ª Nota: '))
nota3 = float(input('Digita a 3ª Nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'A média foi {media}')
    print('O aluno foi Aprovado')
elif media < 6 and media >= 4:
    print(f'A média foi {media}')
    print('O aluno está em recuperação')
else:
    print(f'A média foi {media}')
    print('O aluno foi Reprovado')