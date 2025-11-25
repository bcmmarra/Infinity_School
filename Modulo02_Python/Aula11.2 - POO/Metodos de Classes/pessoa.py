# Métodos de Classes - Python Orientado a Objetos
from datetime import datetime

class Pessoa:
    
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print (self.anoAtual - self.idade)
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.anoAtual - ano_nascimento
        return cls(nome, idade)