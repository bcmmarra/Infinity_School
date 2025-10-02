# Faça um programa que peça o comeco e o final, e com um for mostre uma contagem de 1 em 1 para aqueles valores

inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))

# Inicio = inicio, Final = fim (- 1), Como não foi definido Passo = 1 (Definido por Default)
for n in range (inicio, fim+1):
    print(n)
