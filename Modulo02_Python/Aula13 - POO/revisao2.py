class Produto:
    def __init__(self, nome: str, preco: float, desconto: float = 0):
        self.nome = nome
        self.__preco = preco
        self.__desconto = desconto
        self.__preco_liquido = self.calcular_preco_liquido()

    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco: float) -> None:
        self.__preco = novo_preco
        self.__preco_liquido = self.calcular_preco_liquido()

    @property
    def desconto(self) -> float:
        return self.__desconto
    
    @desconto.setter
    def desconto(self, novo_desconto: float) -> None:
        self.__desconto = novo_desconto
        self.__preco_liquido = self.calcular_preco_liquido()

    @property
    def preco_liquido(self) -> float:
        return self.__preco_liquido

    def calcular_preco_liquido(self) -> float:
        return self.__preco - (self.__desconto / 100 * self.__preco)

    def __str__(self):
        return f'{self.nome} - R${self.__preco_liquido:.2f} ({self.__desconto}% OFF)'


controle = Produto('Controle Dualshock', 300.0, 10)
print(controle) # Preço Liquido Condiz com o Preço Bruto e o Desconto

print(f'Preço Bruto: {controle.preco}') # Chama o Getter
controle.preco = 500 # Chama o Setter
print(f'Preço Bruto: {controle.preco}') # Chama o Getter

# Estamos Chamando os Getters dos Atributos
# Porque eles estão privados.
print(controle.preco)
print(controle.desconto)
print(controle.preco_liquido)