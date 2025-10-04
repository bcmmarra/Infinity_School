'''
💡 Exercício 02 – Tempo de vida em dias
Peça a idade do usuário e calcule quantos dias ele já viveu, assumindo 365 dias por ano.
Depois, mostre uma mensagem com f-string.
'''
idade = int(input("Digite a sua idade: "))
dias = idade * 365

print(f"Você já viveu {dias} dias.")