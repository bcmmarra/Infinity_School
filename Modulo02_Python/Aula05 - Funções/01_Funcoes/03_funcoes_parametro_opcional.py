# Definindo uma função com parametros *Opcional
def saudacao(nome = "Usuário"):
    print(f'Olá, {nome}, seja bem-vindo(a)!')

# Chamando a função como argumentos (passando os parametros)
saudacao() # Olá, Usuário, seja bem-vindo(a)!

saudacao('Bruno') # Olá, Bruno, seja bem-vindo(a)!


# Definindo uma função com parametros *Opcional
def saudacao(nome = "Usuário", Sobrenome = ""): # Se tiver 2 parametros o opcional tem que vim no final
#def saudacao(nome = "Usuário", Sobrenome): # Errado
    print(f'Olá, {nome}, seja bem-vindo(a)!')

# Chamando a função como argumentos (passando os parametros)
saudacao() # Olá, Usuário, seja bem-vindo(a)!

saudacao('Gigi') # Olá, Bruno, seja bem-vindo(a)!