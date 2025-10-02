'''
Exercício: Contagem Regressiva
Escreva um programa que solicite ao usuário um número inteiro positivo 
e realize uma contagem regressiva a partir desse número até zero, 
imprimindo cada número no processo.
'''

# Pede a primeira entrada
x = int(input("Digite um número inteiro POSITIVO para a contagem regressiva: "))

# Validação: o loop continua ENQUANTO 'x' for menor ou igual a zero.
# E dentro desse loop, pede-se uma NOVA entrada.
while x <= 0:
    print(f"O número {x} não é positivo. Por favor, digite um número inteiro POSITIVO.")
    x = int(input("Tente novamente: Digite um número positivo e inteiro: "))

# Após o loop de validação, 'x' COM CERTEZA é um número positivo.
# Agora, vamos fazer a contagem regressiva com o while.
# Inicializa o contador para COMEÇAR DO VALOR DE 'x'
contador = x

# O loop continua enquanto o contador for maior ou igual a 0
while contador >= 0:
    print(contador) # Imprime o número atual do contador
    contador -= 1 # Crucial: decrementa o contador para ir para o próximo número (para trás!)

print("FIM!")
print("---- FIM do Programa ----")