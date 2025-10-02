# Peça ao usuário para digitar valores até digitar 0 e mostre o maior valor digitado
# Calcule e mostre a soma de todos os valores acima de R$200

valores = []
maior = []

while True:
    valor = float(input('Digite o valor da despesa: [0]Sair '))

    if valor == 0:
        break
    elif valor > 200:
        valores.append(valor)
    else:
        valores.append(valor)

print('-'*20)
print(f'Os valores digitados são: {valores} ')
print('-'*20)
print(f'O Maior valor digitado foi: {max(valores)} ')
print('-'*20)
print(f'A soma dos valores acima de 200 é: {sum(valores):.2f} ')

