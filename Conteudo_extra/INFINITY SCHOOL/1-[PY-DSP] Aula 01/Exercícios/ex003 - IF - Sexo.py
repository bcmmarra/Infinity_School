'''Exercício 3:
"Crie um programa que verifique se uma letra digitada é 'F' ou 'M', conforme o sexo."'''
#Pedir ao usuário o sexo dele.
sexo = input("Digite o seu SEXO: ")

#Usar a estrutura condicional para verificar qual é o sexo do usuário.
if sexo == "f" or sexo == "F":
    print(f"O seu sexo é Feminimo")
elif sexo == "m" or sexo == "M":
    print(f"O seu sexo é Masculino")
else:
    print(f"O seu sexo é Indefinido")
