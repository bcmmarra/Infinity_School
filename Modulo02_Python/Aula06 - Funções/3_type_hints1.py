# type hints: pequenas anotações que funcionam como documentação do código, deixando claro o que a função espera e o que ela devolve

# Indicação explícita do tipo da variável, não é muito útil, pois a tipagem é determinada automaticamente.
idade: int = 25
nome: str = "Ana"
altura: float = 1.75

# Indicação explícita do tipo da variável, é muito útil no cenário onde o tipo esperado nao pode ser inferido automaticamente, pcomo por exemplo em uma lista de strings, que começa vazia!.

# Lista de Strings
nomes: list[str] = []

for nome in nomes:
    print(nome.upper())

# Dicionário de nomes para idades
idades: dict[str, int] = {"Ana": 25, "João": 30}

## Type Hint em Funções

# Nas funções, o **type hint** se torna ainda mais útil, pois nas funções eles também servem como um tipo de documentação.

def soma(a: int, b: int) -> int:
    return a + b

def exibir_mensagem(mensagem: str) -> None:
    print(mensagem)