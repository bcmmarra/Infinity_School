## Atividade 3
# Crie um dicionário Python representando um produto de loja online (com `nome`, `preço` e `estoque`). 
# Depois, converta-o para JSON e exiba o resultado.

import json

print('Produtos: ')
produto = {}

produto['nome'] = input('Digite o nome do produto: ')
produto['categoria'] = input('Digite a categoria do produto: ')
produto['preco'] = float(input('Digite o preço do produto: R$ '))
produto['estoque'] = int(input('Digite o estoque disponivel do produto: '))

print(produto)

# Converter dicionário para JSON
json = json.dumps(produto)
print(json)
