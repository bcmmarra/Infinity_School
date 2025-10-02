''' 1. Construa um programa no qual um usuário informe a sua 
estatura em metros e o programa converta-a para centímetros.'''

altura = float(input("Digite a sua altura (em metros): "))
altura *= 100
altura = int(altura)
print(f"Sua altura (em cm) é de {altura}cm.")

'''Comentários sobre a resolução
Para resolver esta questão, basta executar uma operação direta
de conversão. Sabendo que o usuário informará uma estatura
em metros, o programa deverá convertê-la para centímetros
apenas multiplicando-a por 100.'''