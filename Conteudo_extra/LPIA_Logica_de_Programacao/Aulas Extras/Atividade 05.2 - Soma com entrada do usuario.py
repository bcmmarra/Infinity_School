'''
Atividade 9 – Soma com entrada do usuário
Peça dois números e mostre:

O resultado da soma
O tipo do resultado

Uma f-string com: A soma de X + Y é Z
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2

print(f'A soma de {n1} + {n2} é {soma}')
print(f'O tipo do resultado é {type(soma)}')