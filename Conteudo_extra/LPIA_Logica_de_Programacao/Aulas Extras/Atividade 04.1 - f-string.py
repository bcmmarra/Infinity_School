# 🧪 Atividade 4.1 – F-String com Expressão
# Peça ao usuário:

# Nome
# Ano de nascimento
# Mostre a idade estimada usando f-string.
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2025

idade = ano_atual - ano_nascimento
print(f"{nome}, você tem aproximadamente {idade} anos.")


