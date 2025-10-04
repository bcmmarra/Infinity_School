'''
Próximo Desafio: While com um Contador
Combine o while com um contador

Exercício: Contagem Progressiva com While

"Faça um programa que solicite ao usuário um número inteiro positivo N. Em seguida, use um laço while para imprimir todos os números inteiros de 1 até N (inclusive N), um em cada linha. Ao final, imprima 'Contagem concluída!'"

Por exemplo, se o usuário digitar 5, o programa deve imprimir:
1
2
3
4
5
Contagem concluída!
Como você usaria um while loop para fazer essa contagem progressiva, lembrando de um contador e da condição de parada?
'''

x = int(input("Digite um número positivo e inteiro: "))
while x <= 0:
    print(f"{x} é negativo, digite um numero positivo")
    x = int(input("Digite um número positivo e inteiro: "))

contador = 1
while contador <= x:
    print(f"O contador é: {contador}")
    contador += 1

print("Contagem concluída!")

print("---- FIM ----")
