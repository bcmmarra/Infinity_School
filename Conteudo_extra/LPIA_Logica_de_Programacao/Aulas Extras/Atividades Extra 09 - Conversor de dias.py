'''
🔹 Exercício 9 – Conversor de dias
Peça ao usuário um número de dias e converta para semanas e dias restantes.
Exemplo: 17 dias = 2 semanas e 3 dias

📌 Dica: // e % serão úteis aqui.
'''

dias_totais = int(input("Digite a quantidade de dias: "))

semana = dias_totais // 7
dias = dias_totais % 7

print (f"{semana} semanas e {dias} dias.")

# Resolução
dias = int(input("Digite a quantidade de dias: "))
semanas = dias // 7
resto = dias % 7

print(f"{dias} dias = {semanas} semanas e {resto} dias.")
