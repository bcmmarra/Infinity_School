'''
2. Agora o mesmo aluno precisa que você construa um programa
para calcular o comprimento de uma circunferência. Para
isso, o aluno informará ao programa o raio da circunferência.
Sabe-se que:
comprimento = 2 * math.pi * raio

Onde:
comprimento é o comprimento da circunferência
2 é uma constante
pi (Pi) é uma constante matemática (aproximadamente 3.14159)
raio é o raio do círculo
'''

import math
print("--- Calculadora de Raio do Círculo ---")
print("Para calcular o Comprimento de uma circunferência, preciso do Raio da circunferência do círculo.")

#--- Sempre que for executar um operação matemática é necessário converter o numero recebido do usuário para float
raio = float(input("Digite o Raio do Círculo: "))

comprimento = 2 * math.pi * raio

# --- Exibir o resultado ---
print("\n--- Resultado ---")
print(f"Raio do círculo: {raio:.2f}") #---    :.2f formata o resultar para 2 casas decimais
print(f"O COMPRIMENTO da circunferência é: {comprimento:.2f} unidades de comprimento.")
print("-----------------------------------------------------")

