'''Faça um programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite uma letra: ')

match letra:
    case 'A' | 'a':
        print(f'A letra "{letra}" é uma VOGAL.')
    case 'E' | 'e':
        print(f'A letra "{letra}" é uma VOGAL.')
    case 'I' | 'i':
        print(f'A letra "{letra}" é uma VOGAL.')
    case 'O' | 'o':
        print(f'A letra "{letra}" é uma VOGAL.')
    case 'U' | 'u':
        print(f'A letra "{letra}" é uma VOGAL.')
    case _:
        print(f'A letra "{letra}" é uma CONSOANTE.')
        
