'''Faça um programa que mostre todos os numeros pares de 1 até 50 (Ambos Inclusos)'''

#solução simples
for i in range(2, 51, 2):
    print(i)

print('FIM Solução Simples')

#solução com IF
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

