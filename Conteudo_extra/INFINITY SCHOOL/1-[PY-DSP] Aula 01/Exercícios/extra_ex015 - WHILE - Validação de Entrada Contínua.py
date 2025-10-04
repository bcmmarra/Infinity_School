'''
Exercício: Validação de Entrada Contínua

"Faça um programa que solicite ao usuário que digite um número positivo. O programa deve continuar pedindo o número ao usuário enquanto ele digitar um número negativo ou zero. Assim que um número positivo for digitado, o programa deve simplesmente imprimir uma mensagem de sucesso e encerrar."

Como você usaria um while loop para garantir que o usuário só consiga avançar depois de digitar um número válido?

'''

x = int(input("Digite um número positivo e inteiro: "))
while x <= 0:
    print(f"{x} é negativo, digite um numero positivo")
    x = int(input("Digite um número positivo e inteiro: "))

print(f"Parabéns o número digitado foi: {x}")

print("---- FIM ----")
