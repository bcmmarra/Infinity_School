# Importa a classe ABC (Abstract Base Class) e o decorador abstractmethod
# para definir classes e métodos abstratos.
from abc import ABC, abstractmethod

# Passo 1: Definir a Classe Base (Abstração)
# -------------------------------------------
class Funcionario(ABC):
    """Classe base abstrata para todos os funcionários.
    
    A herança de 'ABC' a torna abstrata, impedindo que ela seja instanciada
    diretamente e forçando a implementação de seus métodos abstratos nas subclasses.
    """

    # O método construtor __init__ é chamado na criação de qualquer objeto (Gerente ou Desenvolvedor).
    def __init__(self, id, nome, salario,):
        # Atributos "Protegidos" (Encapsulamento fraco em Python)
        # O uso do underline simples ('_') indica que esses atributos devem ser tratados 
        # como protegidos e acessados principalmente dentro da classe ou subclasses.
        self._id = id           # Guarda o identificador do funcionário.
        self._nome = nome       # Guarda o nome.
        self._salario = salario # Guarda o salário base.
        # Influência: Estes atributos são **herdados** e usados por todas as subclasses.

    # Método Abstrato (Abstração e Polimorfismo)
    @abstractmethod
    def calcular_bonus(self):
        """Método que DEVE ser implementado por todas as subclasses.
        
        Não tem lógica aqui, apenas define uma 'interface' obrigatória para que 
        cada tipo de funcionário possa ter seu próprio cálculo de bônus (Polimorfismo).
        """
        pass # Não faz nada aqui; a implementação fica para as subclasses.
    
    # Método Comum (Herança)
    def exibir_detalhes_basicos(self):
        """Método concreto que exibe informações comuns a todos os funcionários.
        
        Ele é **herdado** por todas as subclasses e pode ser chamado por qualquer objeto Funcionario.
        """
        # Utiliza os atributos protegidos para formatar e imprimir os detalhes.
        print(f"ID: {self._id} - Nome: {self._nome} - Salário: R${self._salario:.2f}")

# 🛠️ Passo 2: Implementar as Subclasses (Gerente e Desenvolvedor)
# -----------------------------------------------------------------

# 2.1. Implementando a Subclasse Gerente 👔 (Herança)
class Gerente(Funcionario):
    """Representa um Funcionário específico que é um Gerente."""
    
    # Construtor do Gerente
    def __init__(self, id, nome, salario, departamento_gerenciado):
        # Chamada ao construtor da classe pai (Funcionario) para inicializar
        # os atributos comuns (id, nome, salario). (Herança)
        super().__init__(id, nome, salario)
        # Inicializa o atributo específico de Gerente.
        self._departamento_gerenciado = departamento_gerenciado
        
    # Implementação do Método Abstrato (Polimorfismo)
    def calcular_bonus(self):
        # Implementa o cálculo de bônus específico para Gerentes (10% do salário).
        # Note que ele usa o atributo '_salario' herdado.
        return self._salario * 0.10
    
    # Método específico
    def relatorio_departamento(self):
        """Funcionalidade exclusiva do Gerente."""
        print(f"Gerente {self._nome} está gerindo o departamento: {self._departamento_gerenciado}")

# 2.2. Implementando a Subclasse Desenvolvedor 💻 (Herança)
class Desenvolvedor(Funcionario):
    """Representa um Funcionário específico que é um Desenvolvedor."""
    
    # Construtor do Desenvolvedor
    def __init__(self, id, nome, salario, tecnologias):
        # Chamada ao construtor da classe pai. (Herança)
        super().__init__(id, nome, salario)
        # Inicializa o atributo específico de Desenvolvedor (uma lista de tecnologias).
        self._tecnologias = tecnologias
        
    # Implementação do Método Abstrato (Polimorfismo)
    def calcular_bonus(self):
        # Implementa o cálculo de bônus específico para Desenvolvedores (5% do salário).
        return self._salario * 0.05
    
    # Método específico
    def listar_tecnologias(self):
        """Funcionalidade exclusiva do Desenvolvedor."""
        # Converte a lista de tecnologias em uma string separada por vírgulas.
        tecs = ", ".join(self._tecnologias)
        print(f"Desenvolvedor {self._nome} trabalha com: {tecs}")

# 🚪 Passo 3: Criar a Classe de Agregação e Encapsulamento (Departamento)
# ----------------------------------------------------------------------

class Departamento:
    """Gerencia uma coleção de objetos Funcionario (Composição/Agregação)."""
    
    def __init__(self, nome):
        # Atributo protegido para o nome.
        self._nome = nome
        # Atributo **PRIVADO** ('__') para a lista de funcionários. 
        # Isso é um **Encapsulamento** mais forte; a lista só pode ser alterada ou 
        # acessada por métodos da própria classe `Departamento`.
        self.__funcionarios = []

    # Método para adicionar um objeto Funcionario
    def adicionar_funcionario(self, funcionario):
        """Adiciona um objeto Funcionario (ou sua subclasse) à lista interna. (Agregação)"""
        # Adiciona o objeto (Gerente ou Desenvolvedor) na lista.
        self.__funcionarios.append(funcionario)
        print(f"{funcionario._nome} adicionado ao departamento {self._nome}.")
    
    # Método para exibir detalhes (Polimorfismo e Agregação)
    def exibir_todos_funcionarios(self):
        """Itera sobre a lista de funcionários e chama o método comum herdado."""
        print(f"\n--- Funcionários do {self._nome} ---")
        if not self.__funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        for funcionario in self.__funcionarios:
            # **Polimorfismo** em ação: O mesmo método é chamado, mas ele é o 
            # método **herdado** da classe Funcionario, que é comum a todos.
            funcionario.exibir_detalhes_basicos() 

    # Método para calcular o custo (Agregação e Polimorfismo)
    def calcular_custo_total(self):
        """Calcula a soma de todos os salários e seus bônus polimórficos."""
        custo = 0
        for funcionario in self.__funcionarios:
            # Soma o salário base (acesso protegido é aceitável dentro do sistema).
            custo += funcionario._salario
            # **Polimorfismo** em ação: O mesmo método é chamado, mas ele executa
            # a lógica **específica** (10% para Gerente, 5% para Desenvolvedor) 
            # de cada objeto, garantindo o cálculo correto.
            custo += funcionario.calcular_bonus() 
        return custo

# 🧪 Passo 4: Execução e Teste do Sistema
# ---------------------------------------

# Instanciando a classe Departamento
dpto_ti = Departamento("Tecnologia da Informação") # Cria o objeto 'Departamento'

# Instanciando Gerentes e Desenvolvedores (Herança)
# O objeto 'gerente_prod' é do tipo Gerente, mas TAMBÉM é do tipo Funcionario.
gerente_prod = Gerente(id=101, nome="Alice Silva", salario=5000.00, departamento_gerenciado="Desenvolvimento de Produto")
# O objeto 'dev_backend' é do tipo Desenvolvedor, mas TAMBÉM é do tipo Funcionario.
dev_backend = Desenvolvedor(id=205, nome="Bruno Marra", salario=3500.00, tecnologias=["Python", "Django", "SQL"])
dev_frontend = Desenvolvedor(id=210, nome="Carlos Nuno", salario=3000.00, tecnologias=["JavaScript", "React"])

print("Objetos criados com sucesso!")

# 2. Composição e Encapsulamento
print("\n--- Adicionando Funcionários ---")
# Adicionando os objetos Funcionario (Gerente e Desenvolvedores) ao objeto Departamento
# O objeto 'dpto_ti' está **agregando/compondo** os objetos 'Funcionario' em sua lista interna.
dpto_ti.adicionar_funcionario(gerente_prod)
dpto_ti.adicionar_funcionario(dev_backend)
dpto_ti.adicionar_funcionario(dev_frontend)

# 3. Testando o Polimorfismo e Herança
print("\n--- Teste de Polimorfismo (Cálculo de Bônus) ---")
# O resultado de calcular_bonus() é diferente para Gerente e Desenvolvedor, 
# pois cada subclasse implementou sua própria lógica. (Polimorfismo)
print(f"Bônus de Alice (Gerente, 10%): R${gerente_prod.calcular_bonus():.2f}")
print(f"Bônus de Bruno (Desenvolvedor, 5%): R${dev_backend.calcular_bonus():.2f}")

print("\n--- Teste de Herança e Métodos Específicos ---")
# Chama o método que foi **herdado** da classe Funcionario.
gerente_prod.exibir_detalhes_basicos() 
# Chama o método **específico** da subclasse Gerente.
gerente_prod.relatorio_departamento()
# Chama o método **específico** da subclasse Desenvolvedor.
dev_backend.listar_tecnologias()

# 4. Testando o Sistema de Gerenciamento (Departamento)
print("\n--- Teste do Gerenciamento (Departamento) ---")

# O método de Departamento usa o método herdado 'exibir_detalhes_basicos()' em 
# todos os funcionários, independentemente de serem Gerentes ou Desenvolvedores.
dpto_ti.exibir_todos_funcionarios()

# O método de Departamento usa o método polimórfico 'calcular_bonus()' em 
# todos os funcionários para obter o custo correto de cada um.
custo = dpto_ti.calcular_custo_total()
print(f"\nCusto Total do {dpto_ti._nome} (Salários + Bônus): R${custo:.2f}")