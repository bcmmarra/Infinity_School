'''Faça um programa que peça um numero para o usuário, e mostre na tela o fatorial desse numero. Exemplo:
Entrada: 5
Saída: 1 * 2 * 3 * 4 * 5 = 120
'''

fatorial = 1
numero = int(input('Digite um numero para calcular fatorial: '))

for n in range(1, numero + 1):
	fatorial *= n

print(f'O fatorial de {numero} é {fatorial}')