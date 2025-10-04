'''
5 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem 'Bom Dia!', 'Boa Tarde!' ou 'Boa Noite!' ou 'Valor Inválido!', conforme o caso.'''
print("---- Turno de estudo ----")
#Pedir ao usuário o horário do seu curso.
periodo_das_aulas = input("Digite o turno que você estuda: (M) matutino ou (V) Vespertino ou (N) Noturno: ")

periodo_das_aulas = periodo_das_aulas.lower() #converte a letra digitada de maiuscula para minuscula, e depois faz a verificação da condição, então de o usuário digitar "a" ou "A" o resultado vai ser o mesmo.


if periodo_das_aulas =="m":
    print(f"Bom dia!")
elif periodo_das_aulas =="v":
    print(f"Boa tarde!")
elif periodo_das_aulas =="n":
    print(f"Boa noite!")
else:
    print(f"Valor inválido!")

print("---- FIM - Turno de estudo ----")
