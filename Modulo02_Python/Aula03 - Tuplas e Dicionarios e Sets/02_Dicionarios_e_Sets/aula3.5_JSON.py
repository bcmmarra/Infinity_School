# O Python já vem com uma biblioteca chamada json para transformar dicionários em JSON e vice-versa.

import json

# Dicionário Python
aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Engenharia"
}

# Converter dicionário para JSON
json_string = json.dumps(aluno)
print(json_string)  # {"nome": "Maria", "idade": 20, "curso": "Engenharia"}

# Converter JSON de volta para dicionário
novo_aluno = json.loads(json_string)
print(novo_aluno["curso"])  # Engenharia