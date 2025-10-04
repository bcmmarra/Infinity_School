import os  # Biblioteca para utilizar o Sistema Operacional

# Banco de Dados (Listas de Dicionários)
despesas = []
TEXTO_USER_CONTINUE = "\nAperte <ENTER> para continuar..."

while True:
    os.system("cls")  # Limpar a tela no Windows
    # os.system("clear") # Limpar a tela no MacOS/Linus

    # Menu
    print("=============================")
    print("   Gerenciador de Despesas   ")
    print("=============================")
    print("[1] - Listar Despesas")
    print("[2] - Cadastrar Despesa")
    print("[3] - Editar Despesa")
    print("[4] - Excluir Despesa")
    print("[5] - Sair")
    print("=============================")

    # Input Opção
    opcao = input("Opção: ")
    print("=============================")

    # Opções
    # Listagem
    if opcao == "1":
        # Se não tiver despesas
        if len(despesas) == 0:
            print("Não há despesas cadastradas.")
            input(TEXTO_USER_CONTINUE)
            continue

        # Mostrando todas as Despesas
        print("Despesas: ")
        for despesa in despesas:
            print(f"- {despesa['titulo']}")
            print(f"Valor: R${despesa['valor']:.2f}")
            print(f"Descrição: {despesa['descricao']}")

    # Cadastro
    elif opcao == "2":
        # Cria o dicionário da despesa
        despesa = {}

        # Preenche o dicionário
        despesa["titulo"] = input("Digite o titulo da despesa: ")
        despesa["valor"] = float(input("Digite o valor da despesa: R$ "))
        despesa["descricao"] = input("Digite a descrição da despesa: ")

        # Adiciona na lista
        despesas.append(despesa)
        print("Despesa cadastrada com sucesso.")

    # Edição
    elif opcao == "3":
        # Lista as depesas para o usuário selecionar qual ele quer editar
        print("Selecione uma Despesa: ")
        for index, despesa in enumerate(despesas):  # Enumera a despesa e seu indíce
            print(f"[{index}] - {despesa['titulo']}")

        print("=============================")
        index = input("-> ")  # Ele digita o indíce da despesa

        # Verifica se é um numero
        if not index.isnumeric():
            print("Despesa Inválida.")
            input(TEXTO_USER_CONTINUE)
            continue

        # Verifica se o indice existe
        index = int(index)
        if index < 0 or index > len(despesas) - 1:
            print("Despesa Inválida.")
            input(TEXTO_USER_CONTINUE)
            continue

        # Busca na lista a despesa (o dicionário) naquele indice
        despesa = despesas[index]
        print("==== Despesa Selecionada ====")
        print(f"- {despesa['titulo']}")
        print(f"Valor: R${despesa['valor']:.2f}")
        print(f"Descrição: {despesa['descricao']}")
        print("=============================")

        # Altera a despesa (o dicionário)
        despesa["titulo"] = input("Digite o novo titulo da despesa: ")
        despesa["valor"] = float(input("Digite o novo valor da despesa: R$ "))
        despesa["descricao"] = input("Digite a nova descrição da despesa: ")

        print("Despesa editada com sucesso.")

    # Exclusão
    elif opcao == "4":
        # Lista as depesas para o usuário selecionar qual ele quer excluir
        print("Selecione uma Despesa: ")
        for index, despesa in enumerate(despesas):  # Enumera a despesa e seu indíce
            print(f"[{index}] - {despesa['titulo']}")

        print("=============================")
        index = input("-> ")  # Ele digita o indíce da despesa

        # Verifica se é um numero
        if not index.isnumeric():
            print("Despesa Inválida.")
            input(TEXTO_USER_CONTINUE)
            continue

        # Busca na lista a despesa (o dicionário) naquele indice
        index = int(index)
        if index < 0 or index > len(despesas) - 1:
            print("Despesa Inválida.")
            input(TEXTO_USER_CONTINUE)
            continue

        # Loop de confirmação da exclusão (Garante que é "S" ou "N")
        while True:
            confirmacao = input("Tem certeza que deseja excluir a despesa? [S/N] ")

            if confirmacao.upper() in {"S", "N"}:
                break

            print("Resposta inválida!")

        # Se ele confirmar que quer excluir com Sim ("S")
        if confirmacao == "S":
            # Remove da lista o elemento no indice escolhido
            despesas.pop(index)
            print("Despesa excluída com sucesso.")
        else:
            # Se não, não remove a despesa
            print("Despesa não foi excluída.")

    # Sair
    elif opcao == "5":
        break

    # Opção Inválida (Não Listada no Menu)
    else:
        print("Opção Inválida!")

    # Input para esperar o usuário para ir para a proxima repetição (voltar para o menu.)
    input(TEXTO_USER_CONTINUE)

print("Fim do Programa!")
