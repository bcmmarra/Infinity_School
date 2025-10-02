'''
Exercício: Somando apenas números pares
Combinar a lógica dos laços com as condicionais que já revisamos:

"Faça um programa que solicite ao usuário um número inteiro positivo N. Em seguida, use um laço for para iterar de 1 até N (inclusive) e calcule a soma de apenas os números pares nesse intervalo. Ao final, imprima a soma total dos números pares."

Por exemplo, se o usuário digitar 7, o programa deve somar 2 + 4 + 6 e imprimir 12.

Como você faria para que o for loop, dentro de cada repetição, decida se o número atual é par e deve ser somado? Lembre-se do operador de módulo (%)!

Sempre que o for precisar percorrer de 1 até x valor usar o range(start, x + 1) que ele vai x=0, x=1, x=2
'''

x = int(input("Digite um número positivo e inteiro: "))

if x < 0:
    print(f"{x} é negativo, digite um numero positivo")
else:
    soma = 0
    for i in range(1, x + 1):
        par = i % 2     #Verificação de Par: par = i % 2 calcula o resto da divisão por 2 e
        if par == 0:    #if par == 0: verifica se o número é par (if i % 2 == 0:, que é o mais comum).
           soma += i
    print(f"A soma dos números pares de 1 até {x} é: {soma}")
    
print("---- FIM ----")
