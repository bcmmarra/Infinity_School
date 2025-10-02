'''
"Faça um programa que solicite ao usuário um número inteiro positivo N. Usando um laço while, calcule a soma de todos os números ímpares de 1 até N (inclusive N). Garanta que o programa só prossiga se o usuário digitar um número positivo."

Por exemplo, se o usuário digitar 7, o programa deve somar 1 + 3 + 5 + 7 e imprimir 16.

Como você adaptaria a lógica do while loop e a verificação de números (agora ímpares) para resolver este desafio?
'''
# 1. Pede a primeira entrada
x = int(input("Digite um número inteiro POSITIVO para somar os ímpares: "))

# 2. Validação: o loop continua ENQUANTO 'x' for menor ou igual a zero.
#    E dentro desse loop, pede-se uma NOVA entrada.
while x <= 0:
    print(f"O número {x} não é positivo. Por favor, digite um número inteiro POSITIVO.")
    x = int(input("Tente novamente: Digite um número positivo e inteiro: "))

# 3. Inicializa a variável 'soma' (depois que 'x' é validado)
soma = 0
# 4. Inicializa o contador que vai percorrer os números de 1 até 'x'
contador = 1

# 5. Loop para calcular a soma dos ímpares de 1 até 'x'
while contador <= x: # Enquanto o contador for menor ou igual a 'x'
    # Verifica se o número atual (contador) é ímpar
    if contador % 2 != 0: # Se o resto da divisão por 2 NÃO for 0, é ímpar
        soma += contador # Adiciona o número ímpar à soma
    
    contador += 1 # MUITO IMPORTANTE: Incrementa o contador para evitar loop infinito e avançar

# 6. Imprime o resultado final (com a mensagem correta)
print(f"A soma dos números ímpares de 1 até {x} é: {soma}")
    
print("---- FIM do Programa ----")