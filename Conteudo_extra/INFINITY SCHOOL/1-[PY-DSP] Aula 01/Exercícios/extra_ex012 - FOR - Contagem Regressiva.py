'''
Exercício: Contagem Regressiva
"Faça um programa que solicite ao usuário um número inteiro positivo. Em seguida, use um laço for para imprimir uma contagem regressiva a partir desse número até 0, exibindo 'FIM!' ao final da contagem."

Por exemplo, se o usuário digitar 5, o programa deve imprimir:

5
4
3
2
1
0
FIM!
Como você faria para que o for loop fizesse essa contagem regressiva? Lembre-se da função range() e de como ela pode ser usada para contar para trás!
'''

n = int(input("Digite um número positivo e inteiro: "))

if n < 0:
    print("O número digitado não é positivo. Por favor, digite um número inteiro POSITIVO.")
else:
    for i in range(n, -1, -1):
        print(i)
    print("FIM!")
    
print("---- FIM ----")