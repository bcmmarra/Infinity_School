# Faça um programa que leia o nome e 4 notas de um aluno, armazena as notas em uma lista, ao final mostre o nome do aluno, as notas e a media na tela

aluno = input('Digite o nome do aluno:')
notas = []
qtd_notas = int(input('Quantas notas vamos calcular? '))

for nota in range(qtd_notas):
    nota = float(input(f'Digite a {nota+1}ª nota: '))
    notas.append(nota)

print('Média', sum(notas) / len(notas))


print(notas)


