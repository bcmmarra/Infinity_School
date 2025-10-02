#resposta = "S"

resposta = input("Deseja continuar? (S/N): ")

if resposta.upper() != "S" and resposta.upper() != "N":
    print('Resposta inválida. Digite (S/N): ')

else:
    while resposta.upper() != "N":
        print("Executando tarefa...")
        resposta = input("Deseja continuar? (S/N): ")




