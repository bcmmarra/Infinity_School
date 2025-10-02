'''
7. Uma imobiliária paga aos seus corretores um salário base de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 5% do valor de cada venda. Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas. Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.
'''

print("--- Calcular Salário Final ---")

# --- Valores padrões ---
salario_base = 1500.00
comissao = 200.00
premio = 1.05

# --- Obter os valores ---
nome = input(f"Digite o seu nome: ")
qnt = float(input(f"Digite a quantidade de imóveis vendidos: "))
valor = float(input(f"Digite o valor total de suas vendas: "))

# --- Calcular o salário final ---
comissao *= qnt
premio = valor * premio
salario_final = salario_base + comissao + premio

# --- Exibir os resultados ---
print(f"\n--- A quantidade de imóveis vendidos foi de: {qnt} unidade(s)")
print(f"\n--- A comissão foi de: {comissao:.2f}")
print(f"\n--- O premio foi de: {premio:.2f}")
print(f"\n--- O valor total das vendas foi de: R$ {valor:.2f}")
print(f"\n--- O Salário Final do Vendedor {nome} foi de: R$ {salario_final:.2f}")
print("------------------------------------------")