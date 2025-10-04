'''"Exercício 4:
"Faça um programa que verifique se uma letra digitada é vogal ou consoante."'''
#Pedir ao usuário a uma letra.
letra = input("Digite uma letra: ")
letra = letra.lower() #converte a letra digitada de maiuscula para minuscula, e depois faz a verificação da condição, então de o usuário digitar "a" ou "A" o resultado vai ser o mesmo.

#Usar a estrutura condicional para verificar qual é a letra digitada.
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra digitada é uma VOGAL")
else:
    print(f"A letra digitada é uma CONSOANTE")
