'''Exercício 5:
 Faça um programa para a leitura de quatro notas de um aluno. O programa deve calcular a média alcançada apresentar:
 a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 b. A mensagem "Reprovado", se a média for menor do que sete;
 c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
print("---- Média das notas ----")
#Pedir ao usuário as Notas do Aluno.
prova1 = float(input("Digite a nota da Prova 1: "))
prova2 = float(input("Digite a nota da Prova 2: "))
prova3 = float(input("Digite a nota da Prova 3: "))
trabalho1 = float(input("Digite a nota do Trabalho 1: "))
trabalho2 = float(input("Digite a nota do Trabalho 2: "))
atividade1 = float(input("Digite a nota da Atividade 1: "))
atividade2 = float(input("Digite a nota da Atividade 2: "))
atividade3 = float(input("Digite a nota da Atividade 3: "))

media_provas = (prova1 + prova2 + prova3) / 3
media_trabalho = (trabalho1 + trabalho2) / 2
media_atividade = (atividade1 + atividade2 + atividade3) / 3

media_final = (media_provas + media_trabalho + media_atividade) / 3

print(f"A média é {media_final:.2f}")

#a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
if media_final >= 7 and media_final < 10:
    print("O Aluno foi Aprovado")
#c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
elif media_final == 10.00:
    print("O Aluno foi Aprovado com Distinção")
#b. A mensagem "Reprovado", se a média for menor do que sete;
else:
    print("O Aluno foi Reprovado")

print("---- FIM - Média das notas ----")
