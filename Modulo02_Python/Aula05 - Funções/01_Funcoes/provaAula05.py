def somar_pares(*args):
    return sum(num for num in args if num % 2 == 0)


# Exemplo de uso:
resultado = somar_pares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"A soma dos pares é: {resultado}")