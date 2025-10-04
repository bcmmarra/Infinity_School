numero = int(input('Digite um numero: '))

# Testa Primeiro o SE
if numero == 0:
	print('O numero é neutro')

# Depois testa o SENÃO SE
elif numero <= 0:
	print('O numero é negativo')

# Se não cair em nenhuma das condições 
# anteriores, ele cai no SENÃO
else:
	print('O numero é positivo')