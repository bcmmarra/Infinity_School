'''
- O valor que será testado vem após `match`.
- Cada `case` representa uma possível correspondência.
- O caractere `_` (underline) representa um **caso coringa** — ou seja, é executado se **nenhum dos casos anteriores for verdadeiro**.
'''

comando = "iniciar"

match comando:
    case "iniciar":
        print("O sistema está iniciando...")
    case "parar":
        print("O sistema está sendo encerrado.")
    case "reiniciar":
        print("Reiniciando o sistema.")
    case _:
        print("Comando não reconhecido.")
