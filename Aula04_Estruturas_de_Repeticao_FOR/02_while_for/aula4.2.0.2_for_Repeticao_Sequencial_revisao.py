soma = 0 #variavel auxiliar

qtd_notas = int(input('Quantas notas você quer a média? '))

for n in range(qtd_notas):
	nota = float(input(f'Digite a {n+1}ª nota: '))
	soma += nota
	
media = soma / qtd_notas
print(f'A média das {n} notas é {media:.2f}')
