# [PY-A03] Crie um programa que armazene alunos (nome, notas) em um dicionário e calcule a média de cada um. Exiba os aprovados (média ≥ 7). 

alunos = {}

while True:
    aluno = input('Digite o nome do aluno (ou [Sair] para encerrar o programa): ').upper()
    
    if aluno == "SAIR":
        break
    
    qnt_notas = int(input('Quantas notas vamos inserir? '))
    notas=[]
    for i in range (qnt_notas):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        notas.append(nota)    

    if notas:
        alunos[aluno] = {
            'notas': notas
        }
        print(f"Aluno {aluno} adicionado com sucesso!\n")
        
for nome_aluno, notas_aluno in alunos.items():
    notas = notas_aluno['notas']
    media = sum(notas) / len(notas)
    
    if media >= 7:
        print(f'O aluno(a) {nome_aluno} foi APROVADO(A) com média {media:.2f}.')
    