'''
🔹 Exercício 10 – Boletim do aluno
Peça 3 notas (com input() e float), calcule a média e exiba:
Média: 6.5
Aprovado (se média >= 6), ou Reprovado (se < 6)

📌 A lógica de condição será usada na Aula 2, mas aqui serve para treinar cálculo e print.
'''

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print (f"Média: {media:.2f}")

# Resolução
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
