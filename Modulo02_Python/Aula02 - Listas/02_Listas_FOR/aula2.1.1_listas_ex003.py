# Crie um programa que peça 10 numeros, e armazene-os em duas listas: `pares` e `impares`. 
# Ao final mostre as duas listas.

# Primeira Versão
par = []
impar = []

for n in range(10):
    numero = int(input('Digite um número: '))
    print(f'Número digitado: {numero}')

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'PAR', par)
print(f'ÍMPAR', impar)


# Segunda Versão
par = ['Nenhum valor PAR foi digitado...']
impar = ['Nenhum valor IMPAR foi digitado...']

for n in range(3):
    numero = int(input('Digite um número: '))
    while numero == 0:
        print('O número digitado precisa ser maior que ZERO')
        numero = int(input('Digite um número: '))
    
    if numero % 2 == 0:
        par.append(numero)
        par.pop(0)
    else:
        impar.append(numero)
        par.pop(0)

print(f'PAR', par)
print(f'IMPAR', impar)

