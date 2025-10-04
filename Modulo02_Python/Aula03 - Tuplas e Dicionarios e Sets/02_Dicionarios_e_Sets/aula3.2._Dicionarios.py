# Exemplo de lista telefônica
telefones = {
    "Ana": "9999-1234",
    "João": "8888-4321",
    "Maria": "9777-5678"
}

print(telefones)

### Acessando Valores
# Para acessar um valor em um dicionário, usamos a **chave.**

print(telefones["Ana"]) # Vai buscar o valor da chave Ana "9999-1234", se a chave não exister vai dar erro KeyError

print(telefones.get("Ana")) # "9999-1234"
print(telefones.get("Carlos")) # None
# Ao utilizar o .get() por padrão ele retorna None caso a chave não exista, se ela existir retorna o valor.


### Adicionando e Atualizando Valores
# Podemos inserir ou atualizar um valor simplesmente atribuindo a uma chave:

telefones["Carlos"] = "9666-2222"  # Se a chave não exister ele cria uma nova chave
telefones["João"] = "9000-0000"    # Se a chave existir ele atualiza o número do da chave


### Removendo Valores
# Para remover um item usamos o método `.pop()`, passando a chave:
telefones.pop("Maria")
print(telefones)


print(telefones.keys())   # dict_keys(['Ana', 'João', 'Carlos'])
print(telefones.values()) # dict_values(['9999-1234', '9000-0000', '9666-2222'])
print(telefones.items()) # dict_items([('Ana', '9999-1234'), ('João', '8888-4321'), ('Maria', '9777-5678')])


cliente = {}

print(cliente)

cliente['']





produtos = {}

for n in range(3):
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    produtos[nome] = preco

print(produtos)
