'''
Categoria 1: Variáveis e Tipos
🧪 Atividade 6 – Cadastro simples
Crie um programa que armazene os seguintes dados:

Nome do usuário
Curso que está estudando

Ano atual
E imprima com uma frase personalizada usando f-string.

📌 Exemplo esperado:
Joana está estudando Python em 2025.
'''

nome = input("DIgite o seu nome: ")
curso = input("Digite o seu curso: ")
escola = input("Em qual escola você estuda: ")
ano = int(input("Digite o ano atual: "))

print(f'{nome} está estudando {curso} na escola {escola} em {ano}')