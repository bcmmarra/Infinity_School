'''Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades

12 = 1 dezena e 2 unidades

Testar com:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 100 = 1 centena
# 300 = 3 centenas.
# 320 = 3 centenas e 2 dezenas
# 310 = 3 centenas e 1 dezena
# 305 = 3 centenas e 5 unidades
# 301 = 3 centenas e 1 unidade
# 101 = 1 centena e 1 unidade
# 311 = 3 centenas, 1 dezena e 1 unidade
# 111 = 1 centena, 1 dezena e 1 unidade
# 25 = 2 dezenas e 5 unidades
# 20 = 2 dezenas
# 10 = 1 dezena
# 21 = 2 dezenas e 1 unidade
# 11 = 1 dezena e 1 unidade
# 1 = 1 unidade
# 7 = 7 unidades
# 16 = 1 dezena e 6 unidades
# '''

numero = int(input('Digite um número menor que 1000: '))
centena = numero // 100
dezena =  (numero % 100) // 10
unidade = numero % 10

if numero < 1000:
    print(f'O número informado foi: ')
 
    if centena == 1:
        parte1 = "centena"
    else:
        parte1 = "centenas"

    if dezena == 1:
        parte2 = "dezena"
    else:
        parte2 = "dezenas"

    if unidade == 1:
        parte3 = "unidade"
    else:
        parte3 = "unidades"    
        

    if centena > 0 and dezena > 0 and unidade > 0:
        print(f'{centena} {parte1}, {dezena} {parte2} e {unidade} {parte3}')

    elif centena > 0 and dezena > 0:
        print(f'{centena} {parte1} e {dezena} {parte2}')
        
    elif centena >0 and unidade>0:
        print(f'{centena} {parte1} e {unidade} {parte3}')
            
    elif dezena > 0 and unidade>0:
        print(f'{dezena} {parte2} e {unidade} {parte3}')
        
    elif centena > 0:
        print(f'{centena} {parte1}')

    elif dezena > 0:
        print(f'{dezena} {parte2}')

    elif unidade > 0:
        print(f'{unidade} {parte3}')
    

else:
    print(f"{numero} é um número inválido.")
    print("Digite um número menor que 1000.")
   
    