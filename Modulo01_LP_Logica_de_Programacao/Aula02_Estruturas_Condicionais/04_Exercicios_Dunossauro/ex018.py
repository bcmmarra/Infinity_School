'''Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input('Digite um dia xx: '))
mes = int(input('Digite um dia xx: '))
ano = int(input('Digite um dia xxxx: '))

print(f'A data digitada foi: {dia}/{mes}/{ano}')


if ano > 0:
    if mes > 0 and mes <= 12:
        #Meses com 31 dias: Janeiro (1), Março (3), Maio (5), Julho (7), Agosto (8), Outubro (10), Dezembro (12).
        #Se o mês for um desses, o dia pode ir de 1 até 31. A validação é simples: o dia tem que ser menor ou igual a 31.
        if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
            
            if dia <= 31 and dia > 0:
                print(f'A data digitada: {dia}/{mes}/{ano} é Válida')
            else:
                print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')
        
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            
            if dia <= 30 and dia > 0:
                print(f'A data digitada: {dia}/{mes}/{ano} é Válida')
            else:
                print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')
        
        else:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                print('Ano Bisexto')
                if dia <= 29 and dia > 0:
                    print(f'A data digitada: {dia}/{mes}/{ano} é Válida')

                else:
                    print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')
            else:
                print('Ano não é Bisexto')
                if dia <= 28 and dia > 0:
                    print(f'A data digitada: {dia}/{mes}/{ano} é Válida')

                else:
                    print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')
    else:
        print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')
else:
    print(f'A data digitada: {dia}/{mes}/{ano} é Inválida')

print(f'FIM DO PROGRAMA')
