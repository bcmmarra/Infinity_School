'''
Faça um programa que peça uma palavra para o usuário, e depois mostre a quantidade de vogais
que tem na palavra.
Exemplo:
Entrada: “abacate”
Saída: “A palavra tem 4 vogais no total.”
'''

palavra = input('Digite uma palavra: ')
qtd_vogais = 0

for letra in palavra.lower():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        qtd_vogais += 1

print(f'A palavra {palavra} tem {qtd_vogais} vogais no total.')


#Gabarito
qtd_vogais = 0
texto = input('Digite um texto qualquer: ')

for letra in texto:
	# if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'o' or letra.lower() == 'i' or letra.lower() == 'u':
	if letra.lower() in 'aeiou':
		qtd_vogais += 1
            
print(f'A palavra tem {qtd_vogais} vogais no total.')
#O operador in pode ser utilizado para substituir varios or.