'''O usuário irá digitar uma quantidade indefinida de números.
ao digitar um número negativo, você deve mostrar o maior número inserido dentre os digitados anteriormente'''

maior = 0
numero = 0 # Variavel de Controle

while numero >= 0:
    print(f'Maior: {maior}')
    numero = int(input('Digite um numero: '))

    if numero > maior:
        maior = numero

print(f'Ao final, o maior numero inserido foi {maior}')

