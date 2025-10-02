'''
8. Construa um programa que receba do usuário o valor do
salário mínimo atual. Na sequência, o programa deve solicitar
que o usuário informe o valor do seu salário mensal. Ao fim, o
programa deve calcular a quantidade de salários mínimos recebidos
pelo usuário.
'''

print("--- Calcular quantos Salários o funcionário recebe ---")

# --- Valores padrões ---
salario_minimo = 1500.00

# --- Obter os valores ---
salario_base = float(input("Digite o seu salário atual: "))

# --- Calcular qnt de salários ---
qnt_salario = salario_base / salario_minimo

# --- Exibir os resultados ---
print(f"\n--- O Funcionário recebe o equivalente de: {qnt_salario:.2f} salários mínimos por mês")
print("------------------------------------------")