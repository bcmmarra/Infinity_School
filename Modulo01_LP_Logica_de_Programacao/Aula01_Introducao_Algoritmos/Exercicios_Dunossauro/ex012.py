'''
Exercício 12
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

Formula
Gigabytes * 1024
'''

gb = int(input('Digite quanto Gigabytes possui o arquivo: '))

mb = gb * 1024

print(f'Um arquivo de {gb} Gigabytes equivale a {mb} Megabytes')