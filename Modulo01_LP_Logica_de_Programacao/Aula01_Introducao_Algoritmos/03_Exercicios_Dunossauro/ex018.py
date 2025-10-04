'''
Exercício 18
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

#Tamanho do arquivo: O programa deve começar perguntando ao usuário o tamanho do arquivo que ele quer baixar, em MegaBytes (MB). Esse valor precisa ser armazenado em uma variável.
tamanho_arquivo = float(input('Digite o tamanho do arquivo em MegaBytes (MB): '))

#Velocidade da internet: Em seguida, o programa deve perguntar a velocidade do link de internet, em MegaBits por segundo (Mbps). Esse valor também precisa ser armazenado em uma variável.
velocidade_internet = float(input('Digite a velocidade da internet MegaBits (Mbps): '))

#Ajustar as unidades de medida: Este é o passo mais importante. Para fazer o cálculo corretamente, você precisa usar as mesmas unidades. A velocidade da internet é dada em MegaBits, mas o tamanho do arquivo é em MegaBytes. Para converter, lembre-se que 1 Byte = 8 Bits.
megabits = tamanho_arquivo * 8

#Calcular o tempo de download em segundos
#O tempo de download é calculado dividindo o tamanho do arquivo (já ajustado para a mesma unidade da velocidade) pela velocidade do link.
segundo = megabits / velocidade_internet

#Converter o tempo para minutos:
#O exercício pede o tempo em minutos. Como o resultado do passo anterior está em segundos, basta dividir esse valor por 60 para obter o tempo em minutos.
minutos = segundo / 60

print(f'O tempo aproximado de download é de {minutos:.2f} minutos')
