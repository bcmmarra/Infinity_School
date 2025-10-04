'''Exercícios da página 11
Exercício 1:
"Faça um Programa que peça dois números ao usuário e imprima o maior deles." 
Que tipo de estrutura de controle de fluxo você usaria e por quê?'''
#Resposta: Estrutura condicional (if-else).

print("---- Programa que pega dois números e imprime o maior deles. ----")
#Pedir dois números ao usuário.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

#Usar a estrutura condicional para comparar esses dois números.
if num1 > num2:
    print(f"O primeiro número {num1} é maior que o segundo número {num2}")
    #Imprimir qual deles é o maior
    print(f"O número maior é: {num1}")
elif num1 == num2:
    print(f"O primeiro número {num1} é igual ao o segundo número {num2}")
else:
    print(f"O primeiro número {num1} é menor que o segundo número {num2}")
    #Imprimir qual deles é o maior
    print(f"O número maior é: {num2}")