'''
10. Imagine a situação em que existem 2 copos com sucos de fruta.
O primeiro copo está com suco de laranja, enquanto o segundo está com suco de acerola.
Você deseja mudar os sucos de copo, isto é, colocar o suco de laranja no segundo copo e o suco de acerola no primeiro copo.
No entanto, não é desejável que eles se misturem.
Agora, vamos transformar esta situação em um programa.
Nas duas linhas abaixo, nós colocamos o suco de laranja no copo1 e o suco de acerola no copo2:
copo1 = “laranja”
copo2 = “acerola”
Continue o programa de modo a transferir o suco de acerola para o copo1 e o suco de laranja para o copo2.
Ao fim, imprima as variáveis suco1 e suco2.
'''
copo1 = "laranja"
copo2 = "acerola"

print(f"Estado Inicial:")
print(f"Copo 1: {copo1}")
print(f"Copo 2: {copo2}")

# --- Lógica para trocar os sucos ---
# Imagine um terceiro copo vazio para fazer a troca sem misturar
# 1. Despeje o conteúdo do copo1 no copo_temporario
copo_temporario = copo1
# Agora: copo_temporario = "laranja", copo1 = "laranja" (mas vamos esvaziá-lo mentalmente), copo2 = "acerola"

# 2. Despeje o conteúdo do copo2 no copo1 (agora "vazio" da laranja)
copo1 = copo2
# Agora: copo_temporario = "laranja", copo1 = "acerola", copo2 = "acerola" (mas vamos esvaziá-lo mentalmente)

# 3. Despeje o conteúdo do copo_temporario no copo2
copo2 = copo_temporario
# Agora: copo_temporario = "laranja", copo1 = "acerola", copo2 = "laranja"

# --- Imprimir o estado final dos copos ---
print(f"\nEstado Após a Troca:")
print(f"Copo 1: {copo1}")
print(f"Copo 2: {copo2}")
print("-----------------------------------")
