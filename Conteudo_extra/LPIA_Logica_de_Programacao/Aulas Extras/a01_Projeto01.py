# ✔ Projeto 01 - Média de Notas:
# Solicita as notas do usuário e calcula a média
# de quatro notas, exibindo o resultado formatado.
# Solicita as notas do usuário
print("|--------| Cálculo da Média de Notas |--------|")
print("|--------| Digite suas quatro notas: |--------|")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"A sua média é {media:.2f}")

print("|--------| FIM do Programa |--------|")
