#Prova Algoritmos e Variáveis
# Imagine que o advogado está ajudando a calcular uma multa rescisória em caso de demissão sem justa causa. Ele sabe que a multa é de 40% sobre o saldo do FGTS do trabalhador, mas ele precisa calcular se a multa é aplicável, dependendo do tempo de serviço do empregado.

# Desafio:
# A empresa de um cliente do advogado quer saber se o trabalhador tem direito à multa de 40% sobre o saldo do FGTS. Caso o trabalhador tenha trabalhado por mais de 1 ano na empresa, a multa será de 40% sobre o valor do FGTS. Caso contrário, não haverá multa.

# O código deve receber o tempo de serviço do trabalhador e o valor do FGTS, e devolver o valor da multa a ser paga.
# Se o tempo de serviço for superior a 1 ano, aplicar 40% sobre o saldo do FGTS.
# Caso contrário, retornar que não há multa.

# Exemplo:
# Tempo de serviço: 2 anos
# Valor do FGTS: R$ 10.000,00
# Resultado esperado: A multa será de R$ 4.000,00 (40% do FGTS)


print('---------------------- Cálculo Multa Rescisória ----------------------')
print('-' * 70)
print('------------------------ Dados do Funcionário ------------------------\n')

nome = input('Nome do funcionário: ')
tempo_servico = int(input('Digite o tempo de trabalho em meses: (Apenas números): '))


if tempo_servico > 12:
    fgts = float(input('Digite o Saldo do FGTS: R$ '))
    multa = fgts * 0.40
    print(f'O tempo de trabalho foi de {tempo_servico} meses')
    print(f'O funcionário {nome} receberá uma multa de R$ {multa:.2f} (40% do FGTS)')
else:
    print(f'O tempo de trabalho foi de {tempo_servico} meses')
    print(f'O funcionário {nome} não tem multa rescisória para receber')

print('-' * 70)
print('-------------------------- FIM DO PROGRAMA ---------------------------')
