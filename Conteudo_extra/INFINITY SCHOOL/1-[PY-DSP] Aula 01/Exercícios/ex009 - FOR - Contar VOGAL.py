'''
Escreva um programa que solicite ao usuário uma frase e conte quantas vogais (a, e, i, o, u) existem nessa frase.
'''

print("---- Contar VOGAL ----")
frase = input("Digite uma frase: ")
frase = frase.lower() 
vogal = 0

for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogal += 1
print(f"Na frase digitada existem {vogal} vogais!")

print("---- FIM - Contador de VOGAL ----")
