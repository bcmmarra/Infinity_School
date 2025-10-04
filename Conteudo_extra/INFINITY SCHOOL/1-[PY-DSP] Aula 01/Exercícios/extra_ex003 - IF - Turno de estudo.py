'''
3 - "Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem 'Bom Dia!', 'Boa Tarde!' ou 'Boa Noite!' ou 'Valor Inválido!', conforme o caso."'''
print("---- Turno de estudo ----")
#Pedir ao usuário o turno de estudo.
turno = input("Em que turno você estuda? Digite M (matutino), V (vespertino) ou N (noturno): ")
turno = turno.upper() #Converte para maiúscula para facilitar a comparação

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Opção Inválida")
print("---- FIM - Turno de estudo ----")
