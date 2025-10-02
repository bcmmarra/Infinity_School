'''
1. Um aluno iniciou seus estudos em geometria plana e, para
validar se suas respostas estão corretas, solicitou sua ajuda. Sabendo
que Area_triangulo= frac(base * altura)/2 construa um programa para auxiliar esse aluno.

base = input("Digite a Base do Triângulo: ")
altura = input("Digite a Altura do Triângulo: ")

Area_triangulo= (base * altura)/2
'''

# --- Cabeçalho do programa ---
print("--- Calculadora de Área de Triângulos ---")
print("Para calcular a área, preciso da base e da altura do triângulo.")

# --- Solicitar a base do triângulo ---
# --- Recebe os valores do usuário em string ---
base_str = float(input("Digite o valor da BASE do triângulo (em unidades de comprimento): "))
# --- Converte o valor recebido de String para número  ---
base = float(base_str)

# --- Recebe os valores do usuário em string e já converte para número ---
altura = float(input("Digite o valor da ALTURA do triângulo (em unidades de comprimento): "))

# --- Calcular a área ---
# Usando a fórmula: Área = (base * altura) / 2
area = (base * altura) / 2

# --- Exibir o resultado ---
print("\n--- Resultado ---")
print(f"Base do triângulo: {base:.2f}")
print(f"Altura do triângulo: {altura:.2f}")
print(f"A ÁREA do triângulo é: {area:.2f} unidades de área.")
print("---------------------------------------")