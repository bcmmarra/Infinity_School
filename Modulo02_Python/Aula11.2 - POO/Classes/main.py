# Classes - Python Orientado a Objetos - Aula 35 => Otávio Miranda

from pessoa import Pessoa

p1 = Pessoa("Bruno", 35)
print(f'{p1.nome} tem {p1.idade} anos')

p1.falar("POO")
p1.parar_falar()
p1.comer('Banana')

print(f'{p1.nome} nasceu no ano de {p1.get_ano_atual()}')