# Conte quantos números ímpares o usuário digita até digitar zero.

impar = 0
numero = int(input('Digite um número: '))

while numero != 0:
    if numero % 2 == 1:
        impar += 1
        numero = int(input('Digite um número: '))
    else:
        numero = int(input('Digite um número: '))

print(impar)


