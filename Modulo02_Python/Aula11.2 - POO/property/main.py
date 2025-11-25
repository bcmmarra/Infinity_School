# @property - Getters e Setters - Python Orientado a Objetos


from pessoa import Pessoa

p1 = Pessoa("Bruno", 35)
print(p1)
print(p1.nome, p1.idade)

p1 = Pessoa.por_ano_nascimento('Bruno', 1990)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(p1.gera_id())
