class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self, valor: float):
        if valor < self.__salario:
            raise ValueError('Você não pode diminuir o salario.')
        
        aumento_real = valor - self.__salario

        if aumento_real > self.__salario * 0.6:
            raise ValueError('O aumento real não pode ser maior que 60%')

        self.__salario = valor

    def calcular_imposto_renda(self) -> float:
        return self.__salario * 0.1