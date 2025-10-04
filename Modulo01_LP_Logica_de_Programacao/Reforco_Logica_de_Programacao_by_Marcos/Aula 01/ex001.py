# Peça dois números e diga qual é o menor.

numero = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
maior = 0

if numero > numero2:
    maior = numero
else:
    maior= numero2

print(f'O maior numero foi: {maior}')
