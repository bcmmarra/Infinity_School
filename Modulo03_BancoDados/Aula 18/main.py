# import pacientes
import pacientes
import medicos


while True:
    print('Gerenciamento do Hospital')
    print('[1] - Pacientes')
    print('[2] - Médicos')
    print('[3] - Sair')

    opcao = input('Opção: ')

    if opcao == '1':
        pacientes.menu()
    elif opcao == '2':
        medicos.menu()
    elif opcao == '3':
        break
