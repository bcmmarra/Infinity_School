# Crie um dicionário com 3 frutas e seus preços. 

# 1. Exiba o preço de uma fruta específica.
# 2. Adicione mais uma fruta ao dicionário.
# 3. Atualize o preço de uma fruta já existente.

# Crie um dicionário com 3 frutas e seus preços. 
frutas = {
    "Maça" : 10.99,
    "Abacate" : 7.99,
    "Banana" : 3.68
    }

# 1. Exiba o preço de uma fruta específica.
print(f'O valor da Fruta {'Abacate'} é R$ ',frutas["Abacate"])

# 2. Adicione mais uma fruta ao dicionário.
frutas["Morango"] = 22.99
print(frutas)

# 3. Atualize o preço de uma fruta já existente.
frutas["Banana"] = 4.71
print(frutas)



# Crie um dicionário com 3 frutas e seus preços. 
frutas = {
    "Maça" : 10.99,
    "Abacate" : 7.99,
    "Banana" : 3.68
    }


# 1. Exiba o preço de uma fruta específica.
print(f'O valor da Fruta {'Abacate'} é R$ ',frutas.get("Abacate"))

# 2. Adicione mais uma fruta ao dicionário.
fruta = input('Digite uma fruta: ')
preco = float(input('Digite o valor do KG da fruta: R$ '))

frutas[fruta] = preco
print(frutas)

# 3. Atualize o preço de uma fruta já existente.
frutas["Banana"] = 4.71
print(frutas)