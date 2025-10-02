'''
 6 - Faça um Programa que receba 2 números e  em seguida pergunte ao usuário qual operação  ele deseja realizar. O resultado da operação deve  aparecer com uma frase que diga se o número é:
 a. par ou ímpar;
 b. positivo ou negativo
'''
print("---- Operações ----")
#Pedir ao usuário 2 números.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = int(input("Qual operação você deseja fazer? Soma (1), Substração (2), Multiplicação (3) ou Divisão (4) "))

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    if num2 == 0:
        print("Erro: Não é possível dividir por zero!")
        resultado = None # Definir resultado como None para não processar as verificações
    else:
        resultado = num1 / num2
else:
    print("Opção inválida")
    resultado = None # Definir resultado como None para não processar as verificações


print(f"O resultado é {resultado}")

if resultado is not None:
    # a. par ou ímpar;
    if resultado % 2 == 0:
        print("O Resultado é PAR")
    else:
        print("O Resultado é ÍMPAR")

    #b. positivo ou negativo
    if resultado < 0:
        print(f"O número {resultado} é NEGATIVO")
    elif resultado == 0:
        print(f"O número {resultado} é igual a 0")
    else:
        print(f"O número {resultado} é POSITIVO")

print("---- FIM - Operações ----")
