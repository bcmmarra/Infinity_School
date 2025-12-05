class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self._salario = salario

    #Getter
    @property
    def salario(self) -> float:
        return self._salario
    
    #Setter
    @salario.setter
    def salario(self, valor: float):
        if valor < self._salario:
            raise ValueError('Você não pode diminuir o salario.')
        
        aumento_real = valor - self._salario

        if aumento_real > self._salario * 0.6:
            raise ValueError('O aumento real não pode ser maior que 60%')

        self._salario = valor

    def calcular_imposto_renda(self) -> float:
        return self._salario * 0.1