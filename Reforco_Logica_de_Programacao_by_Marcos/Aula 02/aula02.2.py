notas = []

while True:
    nota = float(input('Digite uma nota [0] Sair: '))

    if nota <= 0 :
        break

    notas.append(nota)

media = sum(notas) / len(notas)
print(f'A média de notas é {media:.2f}')

