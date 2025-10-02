# Peça 5 idades e calcule a média.
soma = 0

for i in range(5):
    idade = int(input(f'Digite a {i+1}º idade: '))
    soma += idade

media = soma / 5

print(f'A média das idades é: {media:.2f} anos')

