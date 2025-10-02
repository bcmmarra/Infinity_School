'''
🔹 Exercício 12 – Quantidade de letras no nome
Peça o nome do usuário e mostre:

Quantos caracteres tem
Quantas letras (sem contar espaços)

📌 Dica: use len() e replace(" ", "")
'''

nome = input("Digite seu nome completo: ")
print (f"{len(nome)}")

# Resolução
nome = input("Digite seu nome completo: ")

total_caracteres = len(nome)
total_letras = len(nome.replace(" ", ""))

print(f"Seu nome tem {total_caracteres} caracteres e {total_letras} letras.")
