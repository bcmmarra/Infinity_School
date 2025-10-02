# # [PY-A01] Crie um programa que cadastre 5 alunos (nome e nota) em uma lista de tuplas. Em seguida, exiba o nome do aluno com a maior nota. 

lista_de_alunos = []


for i in range (2):
    nome_aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    lista_de_alunos.append((nome_aluno, nota))

nome_aluno_maior_nota = lista_de_alunos[0][0]
maior_nota = lista_de_alunos[0][1]

for aluno in lista_de_alunos:
    nome_aluno = aluno[0]
    nota_aluno = aluno[1]

    if nota_aluno > maior_nota:
        nome_aluno_maior_nota = nome_aluno
        maior_nota = nota_aluno
         
print(f"O aluno com a maior nota é: {nome_aluno_maior_nota} com a nota {maior_nota}.")