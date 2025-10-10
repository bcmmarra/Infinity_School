# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento negativo. Considere 0 como positivo

def positivo_negativo (n: int) -> str:
    if n >= 0:
        return 'P'
    else:
        return 'N'

n = int(input('Digite um número: '))
resultado = positivo_negativo(n)        # sempre armazenar o retorno em um variavel.

print(resultado)



# Função ternária
def positivo_negativo (n: int) -> str:
    return 'P' if n >= 0 else 'N'

n = int(input('Digite um número: '))
resultado = positivo_negativo(n)        # sempre armazenar o retorno em um variavel.

print(resultado)
