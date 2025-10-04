'''
Hora de otimizar a questão número 3, após ter criado seu programa que conta quantas vogais existem numa frase, implemente mais uma funcionalidade. O programa agora deve imprimir a quantidade de vogais e consoantes encontradas.
'''

print("---- Contar VOGAIS e CONSOANTES ----")
frase = input("Digite uma frase: ")
frase = frase.lower() 
vogal = 0
consoante = 0
consoantes_do_alfabeto = "bcdfghjklmnpqrstvwxyz"

for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogal += 1
    elif letra in consoantes_do_alfabeto:
        consoante += 1

print(f"Na frase digitada existem {vogal} vogais!")
print(f"Na frase digitada existem {consoante} consoantes!")

print("---- FIM - Contador de VOGAIS e CONSOANTES ----")
