'''
🔹 Exercício 3 – Relatório de Cadastro
Peça ao usuário:

Nome completo
Profissão
Idade
Cidade onde mora

Depois, imprima uma frase completa com f-string, como:

Carlos, 34 anos, é programador e mora em Recife.
'''
nome_completo = input("Digite o seu nome completo: ")
profissao = input("Digite a sua Profissão: ")
idade = int(input("Digite a sua idade: "))
residencia = input("Digite o municipio que você mora: ")

print(f"{nome_completo}, {idade} anos, é {profissao} e mora em {residencia}.")

# Resolução
nome = input("Nome completo: ")
profissao = input("Profissão: ")
idade = input("Idade: ")
cidade = input("Cidade: ")

print(f"{nome}, {idade} anos, é {profissao} e mora em {cidade}.")

