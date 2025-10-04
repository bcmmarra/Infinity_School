# Some valores digitados até que a soma ultrapasse 100.

numero = int(input('Digite um número: '))

soma = 0

while soma <= 100 :
    soma += numero
    numero = int(input('Digite um número: '))

print(soma)
print('Prgrama encerrado')