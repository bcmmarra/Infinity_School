'''
[LP-A03] Exercício de Loops: Cálculo de Férias Proporcionais

Um trabalhador pode ter direito a férias proporcionais caso ele tenha trabalhado por um tempo menor que 1 ano. O advogado precisa calcular as férias proporcionais de acordo com os meses trabalhados.

Desafio:
O código deve calcular as férias proporcionais, considerando o tempo de serviço do trabalhador. O valor das férias proporcionais será equivalente a 1/12 do salário por mês trabalhado.
O código deve perguntar o salário mensal do trabalhador.
O código deve perguntar o número de meses trabalhados.
Calcular as férias proporcionais com base nesses dados.

Exemplo:
Salário: R$ 1.200,00
Meses trabalhados: 6
Resultado esperado: Férias proporcionais de R$ 600,00.
'''

print(f'CALCULADORA DE FÉRIAS PROPORCIONAIS')

resposta = input("Iniciar o programa: (S/N): ")

while resposta.upper() != "S" and resposta.upper() != "N":
    print('Resposta inválida. Digite (S/N): ')
    resposta = input("Iniciar o programa: (S/N): ")


while resposta.upper() == "S":
    salario_mensal = float(input('Digite o valor total do Salário: R$ '))
    meses_trabalhados = int(input('Digite quantos meses de trabalho: '))

    ferias_proporcional = 1/12
    valor_proporcional = salario_mensal * ferias_proporcional
    valor_ferias_proporcional = valor_proporcional * meses_trabalhados

    print(f'Salário: R$ {salario_mensal:.2f}')
    print(f'Meses trabalhados: {meses_trabalhados}')
    print(f'Férias proporcionais de R$ {valor_ferias_proporcional:.2f}.')
    
    resposta = input("Informar o próximo: (S): ")

print(f'FIM DO PROGRAMA')
