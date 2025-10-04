'''
Exercício: Soma dos Números de 1 a N
"Faça um programa que solicite ao usuário um número inteiro positivo N. Em seguida, use um laço for para calcular e imprimir a soma de todos os números inteiros de 1 até N (inclusive N)."

Por exemplo, se o usuário digitar 5, o programa deve calcular 1 + 2 + 3 + 4 + 5 e imprimir 15.
'''

n = int(input("Digite um número positivo e inteiro: "))

if n < 0:
    print("O número digitado não é positivo. Por favor, digite um número inteiro POSITIVO.")
else:
    soma = 0
    for i in range(1,n + 1):
        soma += i
    print(f"A soma dos números de 1 até {n} é: {soma}")

print("---- FIM ----")
