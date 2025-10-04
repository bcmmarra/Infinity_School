'''
🔹 Categoria 4: F-Strings e Interação
🧪 Atividade 12 – Perfil profissional
Peça:

Nome
Profissão
Tempo de experiência (em anos)

E mostre:
"Maria trabalha como Analista de Dados há 5 anos."
'''

nome = input("Digite o seu nome: ")
profissao = input("Digite a sua Profissão: ")
experiencia = int(input("Quantos anos você tem de experiência? "))

print(f"{nome} trabalha como {profissao} há {experiencia} anos.")