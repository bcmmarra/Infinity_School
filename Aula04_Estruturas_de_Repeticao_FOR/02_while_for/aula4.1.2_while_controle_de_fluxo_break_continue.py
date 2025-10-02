while True:
    resposta = input("Deseja continuar? (S/N): ")
	
    if resposta != "S" and resposta != "N":
        print('Resposta inválida! Digite [S]im ou [N]ão.')
        continue
    
    if resposta == "N":
        break    
		# Alguma operação...