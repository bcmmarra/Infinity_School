'''
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';
'''
# INICIO - 1ª Validação NOME maior que 3 caracteres;
while True:
    nome = input('Digite um nome: ')
    qtd_letra = 0

    for letra in nome:
        qtd_letra += 1

    if qtd_letra < 3:
        print('Nome inválido, Nome tem que ser maior que 3.')
    else:
        print(f'Nome válido')
        break
# FIM - 1ª Validação NOME maior que 3 caracteres;

# INICIO - 2ª Validação IDADE maior que 0 e menor que 150;
while True:
    idade = int(input('Digite a sua idade: '))
    if idade >= 0 and idade < 150:
        print(f'Idade válida')
        break
    else:
        print('Idade inválida, a Idade deve ser entre 0 e 150 anos.')
# FIM - 2ª Validação IDADE maior que 0 e menor que 150;

# INICIO - 3ª Validação SALÁRIO maior que 0;
while True:
    salario = float(input('Digite um salário: R$ '))
    if salario > 0:
        print(f'Salário válido')
        break
    else:
        print('salário inválido, o Salário deve ser maior uqe 0.')
# FIM - 3ª Validação SALÁRIO maior que 0;

# INICIO - 4ª Validação ESTADO CIVIL 's', 'c', 'v', 'd';
while True:
    estado_civil = input('Digite o seu Estado Civil: [s] Solteiro | [c] Casado | [v] Viúvo | [d] Divorciado: ').lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':       
        if estado_civil == 's':
            print(f'Estado Civil: Solteiro')
            
        elif estado_civil == 'c':
            print(f'Estado Civil: Casado')
        
        elif estado_civil == 'v':
            print(f'Estado Civil: Viúvo')
        
        elif estado_civil == 'd':
            print(f'Estado Civil: Divorciado')            
            
        break
    else:
        print(f'Estado Civil inválido')
# FIM - 4ª Validação ESTADO CIVIL 's', 'c', 'v', 'd';


