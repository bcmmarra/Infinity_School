# Solicite uma palavra até que o usuário digite "sair".

palavra = input('Digite uma palavra: ')

while palavra != 'sair':
    print('Para encerrar o programa digite: sair ')
    palavra = input('Digite uma palavra: ')
    

print('Programa Encerrado...')