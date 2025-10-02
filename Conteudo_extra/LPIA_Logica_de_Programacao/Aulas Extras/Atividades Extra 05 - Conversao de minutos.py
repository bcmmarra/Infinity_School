'''
🔹 Exercício 5 – Conversão de minutos
Peça ao usuário um tempo em minutos e converta para horas e minutos.
Exemplo: 135 minutos = 2 horas e 15 minutos.

Exemplo com 130 minutos:
130 / 60 = 2,1666...
definir a parte da Hora = Parte inteira = 2 horas => divisão inteira
definir a parte dos minutos = Sobra 10 = Modulo
Parte decimal: pegar o resto da divisão sobra 10 Fórmula minutos = minutos_totais % 60)
'''

# Solicita ao usuário o tempo em minutos
minutos_totais = int(input("Digite o tempo em minutos: "))
# Calcula a parte inteira das horas
horas = minutos_totais // 60
# Calcula os minutos restantes
minutos = minutos_totais % 60

# Exibe o resultado
print(f"{minutos_totais} minutos equivalem a {horas} hora(s) e {minutos} minuto(s).")

# Resolução
minutos = int(input("Digite o tempo em minutos: "))
horas = minutos // 60
resto = minutos % 60

print(f"{minutos} minutos = {horas} horas e {resto} minutos.")
