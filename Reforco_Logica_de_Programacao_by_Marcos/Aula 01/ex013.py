# Some todos os números pares de 1 a 20.

soma = 0
for i in range (0, 20, 1):
    if i % 2 == 0:
        soma += i

print(soma)