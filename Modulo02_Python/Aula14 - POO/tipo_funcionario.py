from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(
            self,
            nome: str,
            salario: float,
            setor: str
        ):
        super().__init__(nome, salario)
        self.setor = setor
   
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

        if aumento_real > self._salario * 0.1:
            raise ValueError('O aumento real não pode ser maior que 10%')

        self._salario = valor

    def calcular_imposto_renda(self) -> float:
        return self._salario * 0.12

class Estagiario(Funcionario):
    def __init__(
            self,
            nome: str,
            salario: float,
            supervisor: str
        ):
        super().__init__(nome, salario)
        self.supervisor = supervisor

        def calcular_imposto_renda(self):
            return 0

g1 = Gerente('Bruno', 3.500, 'Licitação')
print(g1.calcular_imposto_renda())

e1 = Estagiario('Gigi', 1000, 'Bruno')
print(e1.calcular_imposto_renda())
