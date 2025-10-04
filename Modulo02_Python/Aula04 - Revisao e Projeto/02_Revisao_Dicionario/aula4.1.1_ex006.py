# Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.)

# 1. Pede o nome do aluno
aluno = input('Digite o nome do aluno: ')

# 2. Cria a lista de notas antes do loop
notas = []

# 3. Pede e armazena as 3 notas
for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

# 4. Calcula a média
media = sum(notas) / len(notas)

# 5. Define a situação do aluno (com base na regra do exercício)
if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

# 6. Cria o dicionário e armazena todas as informações
dicionario_aluno = {
    'nome': aluno,
    'notas': notas,
    'media': media,
    'situacao': situacao
}

# 7. Exibe o dicionário completo
print('\n--- Informações do Aluno ---')
print(dicionario_aluno)