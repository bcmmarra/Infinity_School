'''
Exercício: Tabuada
Vamos para um desafio clássico que combina o que aprendemos sobre loops e operações matemáticas:

"Faça um programa que solicite ao usuário um número inteiro. Em seguida, use um laço for para exibir a tabuada desse número, do 1 ao 10."

Por exemplo, se o usuário digitar 7, o programa deve imprimir:

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
Como você usaria o for loop para resolver este problema?
'''

n = int(input("Digite um número positivo e inteiro: "))

if n < 0:
    print("O número digitado não é positivo. Por favor, digite um número inteiro POSITIVO.")
else:
    for i in range(1, 11, 1):
        print(f"{n} x {i} = {n * i}")
    
print("---- FIM ----")