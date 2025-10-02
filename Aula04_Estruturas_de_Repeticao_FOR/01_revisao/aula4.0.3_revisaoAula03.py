soma = 0 #variável acumuladora
contador = 0

qtd_numeros = int(input('Quantos número você quer somar? '))

while contador < qtd_numeros:

    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1

print(f"A soma total é: {soma}.")