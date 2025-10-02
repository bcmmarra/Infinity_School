# Definindo uma função com parametros *Obrigatório
def saudacao(nome):
    print(f'Olá, {nome}, seja bem-vindo(a)!')

# Chamando a função como argumentos (passando os parametros)
saudacao('Bruno') # Olá, Bruno, seja bem-vindo(a)!
saudacao('Gigi') # Olá, Gigi, seja bem-vindo(a)!

# Usuário passando o argumento (parametro) para a função
nome_input = input('Digite um nome: ')
saudacao(nome_input)
