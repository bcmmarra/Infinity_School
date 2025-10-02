'''Crie um programa que:

1. Peça ao usuário para digitar vários números.
2. Depois pergunte se ele deseja continuar, pare se ele digitar `"N”`
3. No final, mostre a soma de todos os números digitados.'''

soma = 0 #variável acumuladora
resposta = input("Vamos começar? (S/N): ")

while resposta.upper() != "S" and resposta.upper() != "N":
    print('Resposta inválida. Digite (S/N): ')
    resposta = input("Tente novamente. Digite: [S]im / [N]ão. ")

while resposta.upper() == "S":
    numero = int(input("Digite um número: "))
    soma += numero
    resposta = input("Continuar? [S]im / Qualquer tecla para SAIR: ")    
        
print(f"A soma total é: {soma}.")








