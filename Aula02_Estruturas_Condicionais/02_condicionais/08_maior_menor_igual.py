print('---- MAIOR, MENOR ou IGUAL? ----')

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

if num1 > num2:
    (print(f'Entre os números {num1} e {num2}: {num1} é MAIOR'))
elif num2 > num1:
    (print(f'Entre os números {num1} e {num2}: {num2} é MAIOR'))
else:
    (print(f'Os números {num1} e {num2} são IGUAIS'))
