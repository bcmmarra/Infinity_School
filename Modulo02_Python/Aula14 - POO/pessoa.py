from dataclasses import dataclass


# Sem dataclass
# class Pessoa:
#     def __init__(self, nome: str, cpf: str):
#         self.nome = nome
#         self.cpf = cpf

# Com dataclass
@dataclass
class Pessoa:
    nome: str
    cpf: str
