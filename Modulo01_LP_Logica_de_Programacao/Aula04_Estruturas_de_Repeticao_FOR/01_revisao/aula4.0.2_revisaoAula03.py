n = 1
total_alunos = int(input('Quantas médias você quer calcular? '))

while n <= total_alunos:
    nota1 = float((input(f'Digite a 1ª nota do {n}º aluno: ')))
    nota2 = float((input(f'Digite a 2ª nota do {n}º aluno: ')))

    media = (nota1 + nota2) / 2

    print(f'A média do {n}º aluno é: {media:.2f}')
    n += 1

print('Fim do programa')