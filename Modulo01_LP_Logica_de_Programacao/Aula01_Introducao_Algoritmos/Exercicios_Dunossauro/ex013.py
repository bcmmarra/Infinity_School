'''
Exercício 13
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
'''
gb = int(input('Digite quanto Gigabytes possui o arquivo: '))

mb = gb * 1024
kb = gb * 1024 * 1024
print(f'Um arquivo de {gb} Gigabytes equivale a {mb} Megabytes e {kb} Kilobytes')