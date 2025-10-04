'''
💡 Desafios Extras (Mais Avançados)
💡 Exercício 01 – Calculadora de IMC
Peça ao usuário:
Peso (em kg)
Altura (em metros)

Calcule o IMC = peso / (altura²)
Exiba o resultado com 2 casas decimais.
'''

peso = float(input("Digite o seu Peso (em kg): "))
altura = float (input("Digite a sua Altura (em metros):"))

imc = peso / (altura**2)

print(f"O seu IMC é de {imc:.2f}.")