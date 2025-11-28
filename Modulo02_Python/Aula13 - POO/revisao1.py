class Produto:
    def __init__(self, nome: str, preco: float, desconto: float = 0):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
        self.preco_liquido = self.calcular_preco_liquido()

    def calcular_preco_liquido(self) -> float:
        return self.preco - (self.desconto / 100 * self.preco)


controle = Produto('Controle Dualshock', 300.0, 10)

print(controle.nome)
print(controle.preco)
print(controle.preco_liquido)
print(controle.calcular_preco_liquido())

calca = Produto('Calça Sarja', 180)

print(calca.nome)
print(calca.preco)
print(calca.preco_liquido)
print(calca.calcular_preco_liquido())
