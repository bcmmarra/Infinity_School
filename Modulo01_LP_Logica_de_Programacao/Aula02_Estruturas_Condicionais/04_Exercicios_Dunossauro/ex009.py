'''Faça um programa que leia três números e mostre-os em ordem decrescente:'''

n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
n3 = int(input('Digite o 3º Número: '))

if n1 >= n2 and n1 >= n3:
  maior = n1
  if n2 >= n3:
    meio = n2
    menor = n3
  else:
    meio = n3
    menor = n2
elif n2 >= n1 and n2 >= n3:
  maior = n2
  if n1 >= n3:
    meio = n1
    menor = n3
  else:
    segundo = n3
    menor = n1
else:
  maior = n3
  if n1 >= n2:
    meio = n1
    menor = n2
  else:
    segundo = n2
    menor = n1

print(f"Os números em ordem decrescente são: {maior}, {meio} e {menor}")