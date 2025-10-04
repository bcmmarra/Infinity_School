import os
# Projeto!
# Você foi contratado para criar um programa de gerenciamento de despesas!

# 1. Ao iniciar deve mostrar o seguinte menu:
# =============================
#    Gerenciador de Despesas
# =============================
# [1] - Listar Despesas
# [2] - Cadastrar Despesa
# [3] - Editar Despesa
# [4] - Excluir Despesa
# [5] - Sair
# =============================

listaDespesas = []

while True:
    os.system('cls')

    print("""
=============================
Gerenciador de Despesas
=============================
[1] - Listar Despesas
[2] - Cadastrar Despesa
[3] - Editar Despesa
[4] - Excluir Despesa
[5] - Sair
=============================
""")

    opcao=int(input('Opção: '))

    if opcao == 1:
        print("""
=============================
Lista de Despesas
=============================
""")
        if listaDespesas:
            for i, despesa in enumerate(listaDespesas):
                print(f'- [{i+1}] {despesa["Titulo"]} | Valor: R$ {despesa["Valor"]:.2f} | Descrição: {despesa["Descricao"]}')
            input('\nTecler "ENTER" para voltar ao MENU')
        else:
            input('***Nenhuma despesa encontrada***\n\nTecler "ENTER" para voltar ao MENU')

    elif opcao == 2:
        print("""
=============================
Cadastro de Despesas
=============================
""")
        despesa = {}

        despesa['Titulo'] = input('Digite o nome da despesa que deseja inserir: ')
        despesa['Valor'] = float(input('Digite o valor da despesa: R$ '))
        despesa['Descricao'] = input('Digite a descrição: ')

        listaDespesas.append(despesa)
        input('\n***Despesa cadastrada com sucesso***\n\nTecle "ENTER" para voltar ao MENU')

    elif opcao == 3:
        print("""
=============================
Lista de Despesas
=============================
""")
        
        if listaDespesas:
            for i, despesa in enumerate(listaDespesas):
                print(f'- [{i+1}] {despesa["Titulo"]} | Valor: R$ {despesa["Valor"]:.2f} | Descrição: {despesa["Descricao"]}')
                
            index = int(input('\nEscolha o número da despesa que deseja EDITAR: '))

            if index > 0 and index <= len(listaDespesas):
                editar = listaDespesas[index - 1]
                editar['Titulo'] = input(f'Título (atual: {editar["Titulo"]}) - Editar o Título da despesa: ')
                editar['Valor'] = float(input(f'Valor (atual: R$ {editar["Valor"]:.2f}) - Editar o Valor da despesa: R$ '))
                editar['Descricao'] = input(f'Descrição (atual: {editar["Descricao"]}) - Editar a Descrição: ')
                print('Despesa editada com sucesso!')
                
                print('--- Verificação ---')
                print('Nova despesa (dados atualizados):')
                print(f'Título: {editar["Titulo"]}')
                print(f'Valor: R$ {editar["Valor"]:.2f}')
                print(f'Descrição: {editar["Descricao"]}')
                print('-------------------')
                input('Tecler "ENTER" para voltar ao MENU')

            else:
                input('***Despesa não encontrada***\n\nTecle "ENTER" para voltar ao MENU')

        else:
            input('***Nenhuma despesa encontrada***\n\nTecle "ENTER" para voltar ao MENU')
        
    elif opcao == 4:
        print("""
=============================
Lista de Despesas
=============================
""")
        
        if listaDespesas:
            for i, despesa in enumerate(listaDespesas):
                print(f'- [{i+1}] {despesa["Titulo"]} | Valor: R$ {despesa["Valor"]:.2f} | Descrição: {despesa["Descricao"]}')
            
            index = int(input('\nEscolha o número da despesa que deseja EXCLUIR: '))

            if index > 0 and index <= len(listaDespesas):
                excluir = listaDespesas[index - 1]
                confirmacao = input(f'Confirma a EXCLUSÃO da despesa: {excluir["Titulo"]} | Valor: R$ {excluir["Valor"]:.2f} | Descrição: {excluir["Descricao"]}? S[im] N[ão]: ').upper()

                while confirmacao != "S" and confirmacao != "N":
                    print('Resposta inválida. Digite (S/N): ')
                    confirmacao = input(f'Confirma a EXCLUSÃO da despesa: {excluir["Titulo"]} | Valor: R$ {excluir["Valor"]:.2f} | Descrição: {excluir["Descricao"]}? S[im] N[ão]: ').upper()

                if confirmacao == "S":
                    listaDespesas.pop(index-1)
                    print('Despesa excluida com sucesso!')
                    print('\n--- Verificação ---')
                    print('Despesa Excluida):')
                    print(f'Título: {excluir["Titulo"]}')
                    print(f'Valor: {excluir["Valor"]:.2f}')
                    print(f'Descrição: {excluir["Descricao"]}')
                    print('-------------------')

                else:
                    print('Exclusão cancelada')
                
                if listaDespesas:
                    for i, despesa in enumerate(listaDespesas):
                        print(f'- [{i+1}] {despesa["Titulo"]} | Valor: R$ {despesa["Valor"]:.2f} | Descrição: {despesa["Descricao"]}')
                    input('***Despesa excluida com sucesso***\n\nTecle "ENTER" para voltar ao MENU')

                else:
                    print("""
=============================
Lista de Despesas Atualizada
=============================
""")
                    input('***Nenhuma despesa encontrada***\n\nTecle "ENTER" para voltar ao MENU')
                
            else:
                input('***Despesa não encontrada***\n\nTecle "ENTER" para voltar ao MENU')
        else:
            input('***Nenhuma despesa encontrada***\n\nTecle "ENTER" para voltar ao MENU')
        
       
    elif opcao == 5:
        print('Programa encerrado')
        break

    else:
        print('Opção Inválida')
        input('Tecle "ENTER" para escolher outra opção')
