#Entrada
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: '))

#Processamento
media = (nota1 + nota2 + nota3) / 3

#Saída
print(f'A média é {media:.2f}')

if media >= 6:
    print('Status: Aprovado')
elif media < 4:
    print('Status: Reprovado')
else:
    print('Status: Em Recuperação')

