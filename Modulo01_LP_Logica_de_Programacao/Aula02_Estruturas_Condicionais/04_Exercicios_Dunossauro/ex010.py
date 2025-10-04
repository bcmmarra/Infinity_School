'''Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


turno = input("Digite o turno que você estuda(M-matutino ou V-Vespertino ou N- Noturno): ")

match turno:
    case "m" | "M":
        print("Bom dia!")
    case "v" | "V":
        print("Boa tarde!")
    case "n" | "N":
        print("Boa Noite!")
    case _:
        print("Valor Inválido.")

