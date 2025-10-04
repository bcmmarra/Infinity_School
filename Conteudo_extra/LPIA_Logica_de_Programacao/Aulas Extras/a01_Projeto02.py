# ✔ Projeto 02 - Cálculo de Salário por Hora
# Objetivo: Criar um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, calcule o salário total e exiba o resultado (considere que você trabalha 20 dias no mês).

# 1 - Solicitar o Salário Mensal:
# Use a função input() para pedir ao usuário que insira quanto ele ganha por mês. Converta a entrada do usuário de string para um número (float) para permitir cálculos.
salario = float(input("Qual é o seu salário mensal? R$ "))

# 2 - Solicitar o Número de Horas Trabalhadas por Semana:
# Use a função input() para pedir ao usuário que insira o número de horas ele trabalhadas na semana. Converta essa entrada também para (float) para permitir cálculos.
entrada = float(input("Que Horas você entra no trabalho? "))
pausa = float(input("Que Horas você sai para o Almoço? "))
retorno_pausa = float(input("Que Horas você retorna do Almoço? "))
saida = float(input("Que Horas você sai do trabalho? "))
# Calcular o número de horas trabalhadas por dia
hs_dia = (saida - entrada) - (retorno_pausa - pausa)

print(f"Você trabalha {hs_dia:.2f} horas por dia.")

quantidade_dias = int(input("Quantos dias você trabalha por semana? "))
hs = hs_dia * quantidade_dias
print(f"Você trabalha {hs:.2f} horas por semana.")

# 3 - Calcular o Número de Horas Trabalhadas no Mês:
# Multiplique o número de horas trabalhadas por semana por 4 (considerando 4 semanas no mês) para obter o total de horas trabalhadas no mês.
hs_mes = hs * 4

# 4 - Calcular o Valor da Hora Trabalhada:
# Divida o salário mensal pelo total de horas trabalhadas no mês para obter o valor da hora trabalhada.
valor_hora = salario / hs_mes

# 5 - Exibir o Resultado:
# Use a função print() para exibir o valor da hora trabalhada formatado com duas casas decimais.
print(f"O valor da sua hora trabalhada é: R$ {valor_hora:.2f}")

# 6 - Mensagem de Encerramento:
# Exiba uma mensagem de encerramento do programa.

print("|--------| Cálculo do Salário por Hora |--------|")