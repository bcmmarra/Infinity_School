'''
Exercicios Extras

1 - Faça um Programa que leia 3 números e mostre o maior e o menor deles.'''
print("---- Minha Solução ----")
#Pedir ao usuário 3 números.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#Usar a estrutura condicional para comparar esses três números.
if num1 > num2 and num1 > num3:
    print(f"O primeiro número {num1} é o maior")
    if num2 < num3:
        print(f"O segundo número {num2} é o menor")
    else:
        print(f"O terceiro número {num3} é o menor")
elif num2 > num1 and num2 > num3:
    print(f"O segundo número {num2} é o maior")
    if num1 < num3:
        print(f"O primeiro número {num1} é o menor")
    else:
        print(f"O terceiro número {num3} é o menor")
else:
    print(f"O terceiro número {num3} é o maior")
    if num1 < num2:
        print(f"O primeiro número {num1} é o menor")
    else:
        print(f"O segundo número {num2} é o menor")
print("---- FIM - Minha Solução ----")

'''
Funções max() e min()

O que são max() e min()?

max(): É uma função embutida do Python que recebe um número de argumentos (ou uma sequência iterável, como uma lista) e retorna o maior valor entre eles.

min(): De forma semelhante, esta função retorna o menor valor entre os argumentos (ou de uma sequência).

Funcionamento...
Passamos os números que quer comparar diretamente para essas funções. O Python já tem toda a lógica interna para lidar com as comparações, incluindo casos de números iguais.

Vantagens:
Simplicidade: O código fica muito mais curto, limpo e fácil de ler.

Robustez: As funções max() e min() já foram testadas e otimizadas. Elas lidam automaticamente com todos os casos, incluindo números iguais, sem a necessidade de múltiplas condições if/elif/else aninhadas.

Escalabilidade: Se você tivesse 10 ou 100 números para comparar, usar max() e min() continuaria sendo simples (basta colocá-los em uma lista, por exemplo), enquanto a abordagem manual com if/elif se tornaria insustentável.
'''
print("----Funções max() e min()----")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3) # Encontra o maior entre num1, num2 e num3
menor = min(num1, num2, num3) # Encontra o menor entre num1, num2 e num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

print("---- FIM - Funções max() e min() ----")

print("---- Lógica manual ----")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior_num = num1 # Inicializa o maior com o primeiro número
menor_num = num1 # Inicializa o menor com o primeiro número

# Verifica o maior
if num2 > maior_num:
    maior_num = num2
if num3 > maior_num:
    maior_num = num3

# Verifica o menor
if num2 < menor_num:
    menor_num = num2
if num3 < menor_num:
    menor_num = num3

print(f"O maior número é: {maior_num}")
print(f"O menor número é: {menor_num}")

print("---- FIM - Lógica manual ----")
