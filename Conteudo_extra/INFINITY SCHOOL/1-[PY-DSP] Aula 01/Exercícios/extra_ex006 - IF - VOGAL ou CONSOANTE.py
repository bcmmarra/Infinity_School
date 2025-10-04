'''
6 - Faça um Programa que solicite a digitação de uma letra e identifique se ela é uma vogal ou consoante. Além disso, se for consoante, diga quantas consoantes foram digitadas." (Na verdade, a parte de "quantas consoantes foram digitadas" talvez seja de um exercício mais avançado ou com laços de repetição, então vamos focar na primeira parte por enquanto: "identifique se ela é uma vogal ou consoante".)'''

print("---- Identificar a letra, VOGAL ou CONSOANTE ----")
#Pedir ao usuário o horário do seu curso.
letra = input("Digite uma letra: ")
letra = letra.lower() #converte a letra digitada de maiuscula para minuscula, e depois faz a verificação da condição, então de o usuário digitar "a" ou "A" o resultado vai ser o mesmo.

#Usar a estrutura condicional para verificar qual é a letra digitada.
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra digitada é uma VOGAL")
else:
    print(f"A letra digitada é uma CONSOANTE")


print("---- FIM - Identificar a letra, VOGAL ou CONSOANTE ----")
