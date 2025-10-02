'''
[LP-A02] Exercício de Condicionais: Verificação de Jornada de Trabalho
Imagine que o advogado está ajudando a verificar se o trabalhador está cumprindo corretamente a jornada de trabalho. A jornada padrão é de 44 horas semanais.

Desafio:
O advogado precisa verificar se um trabalhador cumpriu a jornada de trabalho corretamente. O código deve verificar se as horas trabalhadas ultrapassaram as 44 horas semanais. Se sim, será necessário pagar horas extras (o valor da hora extra é 50% a mais do valor da hora normal).

Perguntar ao usuário o total de horas trabalhadas na semana.

Caso as horas trabalhadas sejam superiores a 44, o programa deve calcular o valor das horas extras a serem pagas (se o valor da hora normal for informado pelo usuário).

Se não houver horas extras, deve exibir uma mensagem dizendo que a jornada foi cumprida corretamente.

Exemplo:
Horas trabalhadas: 50
Valor da hora normal: R$ 15,00
Resultado esperado: 6 horas extras a R$ 22,50 cada.
'''

print(f'CALCULADORA DE HORA EXTRA')

horas_semana = float(input('Digite quantas horas trabalhou essa semana: '))
vlr_hora_normal = float(input('Digite o valor da hora: R$ '))
jornada_normal = 44
percentual_hora_extra = 1.50

if horas_semana > 44:
    hora_extra = horas_semana - jornada_normal
    valor_hora_extra = vlr_hora_normal * percentual_hora_extra
    pagamento_hora_extra = hora_extra * valor_hora_extra

    print(f'Horas trabalhadas: {horas_semana:.2f}')
    print(f'Valor da hora normal: {vlr_hora_normal:.2f}')
    print(f'Resultado esperado: {hora_extra:.2f} horas extras a R$ {valor_hora_extra:.2f} cada.')
    print(f'Valor a ser pago em Horas Extras é R$ {pagamento_hora_extra:.2f}.')

else:
    print(f'Horas trabalhadas: {horas_semana:.2f}hs')
    print(f'Jornada normal completa')

print(f'FIM DO PROGRAMA')
