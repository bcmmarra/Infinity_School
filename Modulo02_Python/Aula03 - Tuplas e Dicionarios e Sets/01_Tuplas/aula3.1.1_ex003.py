# Atividade 07
# Crie uma lista chamada cores com 4 cores.
# Utilize o enumerate para percorrer essa lista e exibir o índice junto com o valor, no formato:
# 0 - vermelho
# 1 - azul
# 2 - verde
# 3 - amarelo

# Lista
cores = ['vermelho', 'azul', 'verde', 'amarelo']

for index, cor in enumerate(cores):
	print(f'{index} - {cor}')
 