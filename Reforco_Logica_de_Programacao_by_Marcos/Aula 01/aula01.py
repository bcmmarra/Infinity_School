try:
    numero = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    print(numero + numero2)
except ValueError:
    print('Você deve digitar apenas número')

