# Crie uma classe Funcionario com os seguintes requisitos:

# - Atributos:
#     - nome (público)
#     - __salario (privado)
# - Métodos:
#     - @property salario → retorna o salário
#     - @salario.setter → atualiza o salário, mas com algumas regras
#         - o salário não pode ser menor que o valor anterior.
#         - o aumento não pode ser maior que 60% do valor anterior.
#     - calcular_imposto_renda() → deve retornar 10% do salário

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.__salario = salario
    
    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario: float) -> None:
        if novo_salario < self.__salario:
            raise ValueError(f'O novo salário: {novo_salario} não pode ser menor que o salário atual {self.__salario}')
            
        aumento_real = novo_salario - self.__salario
        aumento_maximo = self.__salario * 0.60

        if aumento_maximo < aumento_real:
            raise ValueError('O aumento não pode ser maior que 60% do salário atual.')
        
        self.__salario = novo_salario

    def calcular_imposto_renda(self) -> float:
        return self.__salario * 0.10


nome = input('Digite o nome do funcionário: ')
salario_inicial = float(input('Digite o salário inicial do funcionário: '))

funcionario = Funcionario(nome, salario_inicial)

print(f'Funcionário: {funcionario.nome}')
print(f'Salário: {funcionario.salario}')

novo_salario = float(input('Digite o novo salário do funcionário: '))

try:
    funcionario.salario = novo_salario
    print('Salário Atualizado com Sucesso.')
except ValueError as err:
    print(err)

print(f'Funcionário: {funcionario.nome}')
print(f'Salário: {funcionario.salario}')
print(f'Imposto de Renda: {funcionario.calcular_imposto_renda()}')