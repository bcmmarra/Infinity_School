'''
Escreva um programa que possa verificar uma sequência de 10 números  se são par ou ímpar.
'''
print("---- Verificador de Números Pares ou Ímpares (10 números) ----")
# O loop 'for' vai rodar EXATAMENTE 10 vezes (de 0 a 9, ou de 1 a 10 se preferir)
for contagem in range(1, 11): # Isso garante que vamos pedir 10 números
    # A cada repetição, pedimos um novo número ao usuário
    numero = int(input(f"Digite o {contagem}º número: "))

    # Agora, verificamos SE ESSE 'numero' digitado é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
    
    print("-" * 20) # Apenas para separar a saída de cada número

print("---- FIM da Verificação ----")



print("---- FIM ----")
