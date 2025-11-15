# Conceitos Fundamentais da POO

# Classes e Objetos
# Classe: É o molde ou a planta para criar objetos.
# Ela define:
# Características (atributos)
# Comportamentos (métodos)

# Que todos os objetos desse tipo terão.
# Exemplo:
# Caracteristicas: A classe Cachorro define que todo cachorro tem nome, idade, raça e cor
# Comportamentos: Pode latir ou comer.

# Objeto (ou Instância)
# É uma ocorrência concreta da classe.
# É o item real criado a partir do molde.

# Exemplo: O objeto cao1 e cao2 é uma instância específica da classe Cachorro, onde cao1 tem o nome='Rex', idade=5, raca='Vira-lata' e cor='caramelo'.

# Nota: O parâmetro self é uma referência à instância (o objeto) atual. Ele deve ser o primeiro parâmetro de qualquer método de instância.

class Cachorro:
    # Atributo de Classe (compartilhado por todas as instâncias)
    especie = "Canis familiaris"

    # Método Construtor (__init__)
    # Usado para inicializar o objeto e definir atributos de instância
    def __init__(self, nome, idade, raca, cor):
        # Atributos de Instância (únicos para cada objeto)
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
    
    # Método (Comportamento)
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")
    
    def comer(self):
        print(f"{self.nome} está comendo!!!")

# Criação de Objetos (Instanciação)
cao1 = Cachorro("Rex", 5, "Vira-lata", "Caramelo")
cao2 = Cachorro("Mila", 3, "Poodle", "Branco")

# Acessando Atributos
print(f"O nome do primeiro cão é {cao1.nome} e ele tem {cao1.idade} anos.")
print(f"A espécie de cao2 é {cao2.especie}.")

# Chamando Métodos
cao1.latir()
cao2.comer()


# ========================================================================================================

# O coração da POO reside em quatro pilares principais. Pense neles como as regras de ouro para construir seu software.
# - Encapsulamento
# - Herança
# - Polimorfismo
# - Abstração

# 1 - Encapsulamento
# O Encapsulamento é o princípio de agrupar dados (atributos) e os métodos que operam nesses dados em uma única unidade (a classe) e restringir o acesso direto a alguns dos componentes do objeto.

# Objetivo: Proteger os dados de modificações externas acidentais ou não intencionais e esconder a complexidade interna da classe.

# Python não possui modificadores de acesso estritos (private, public) como outras linguagens. A convenção é usar underscores:

# Público: Atributos sem prefixo. Acesso direto permitido (self.nome).
# Protegido: Prefixo com um único underscore _ Sugere que o acesso direto deve ser evitado (self._cor).
# Privado: Prefixo com dois underscores __ Python faz uma "name mangling" (mecanismo para dificultar o acesso direto) para tornar o acesso mais difícil (self.__saldo).

# Prática: Encapsulamento com Propriedades

# Usamos getters e setters (métodos para obter e definir valores) para controlar o acesso e a modificação de atributos internos, geralmente usando o decorador @property.

class ContaBancaria:
    def __init__(self, saldo_inicial):
        # Atributo "privado"
        self.__saldo = saldo_inicial 

    # Getter: Permite que você leia o valor
    @property
    def saldo(self):
        return self.__saldo

    # Método de controle: Única forma de alterar o saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("O valor do depósito deve ser positivo.")

# Uso
conta = ContaBancaria(1000)
print(f"Saldo inicial: R${conta.saldo:.2f}") # Acessa via @property (getter)
conta.depositar(500)
print(f"Novo saldo: R${conta.saldo:.2f}")

# Tentativa de acesso direto (desencorajado e mais difícil devido ao __)
# print(conta.__saldo) # Tentar acessar o item (atributo) diretamente retorna um erro!


# ========================================================================================================

# Herança
# A Herança permite que uma nova classe (subclasse ou classe filha) absorva os atributos e métodos de uma classe existente (superclasse ou classe pai).

# Objetivo: Promover a reutilização de código e estabelecer uma relação "É UM TIPO DE" (ex: Um Gato É UM TIPO DE Animal).

# Prática: Demonstração de Herança

class Animal: # Superclasse (ou Classe Pai)
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f"{self.nome} está comendo.")

class Gato(Animal): # Subclasse (ou Classe Filha) que herda de Animal
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai para inicializar 'nome'
        super().__init__(nome) 
        self.raca = raca
    
    def miar(self):
        print(f"{self.nome} da raça {self.raca} está miando: Miau!")

# Uso
bichano = Gato("Frajola", "Siamês")

# Métodos herdados da classe Animal
bichano.comer() 

# Método específico da classe Gato
bichano.miar() 

print(f"O nome é {bichano.nome}")


# ========================================================================================================


# Polimorfismo
# O Polimorfismo (que significa "muitas formas") permite que objetos de classes diferentes sejam tratados de maneira uniforme, ou que um método tenha diferentes implementações dependendo do objeto que o chama.

# O polimorfismo é naturalmente suportado através da Sobrescrita de Métodos (Overriding) e Duck Typing (Se anda como um pato e faz quack como um pato, deve ser um pato).

# Prática: Polimorfismo (Sobrescrita de Método)

class Passaro(Animal):
    def fazer_som(self):
        print("O pássaro está cantando.")

class Pato(Animal):
    # Sobrescrita (Overriding) do método fazer_som
    def fazer_som(self): 
        print("O pato faz Quack! Quack!")

class Cachorro_poli(Animal):
    # Sobrescrita (Overriding) do método fazer_som
    def fazer_som(self):
        print("O cachorro faz Au Au!")

# Função que aceita qualquer objeto que tenha o método 'fazer_som'
def descrever_som(animal):
    animal.fazer_som()

p = Passaro("Piu")
d = Pato("Donald")
c = Cachorro_poli("Pluto")

# Chamada polimórfica: a mesma função chama o método correto de cada objeto
descrever_som(p) 
descrever_som(d)
descrever_som(c)

# ========================================================================================================

# Abstração
# A Abstração é o ato de esconder a implementação complexa e mostrar apenas as informações essenciais e relevantes ao usuário.

# Objetivo: Focar no que um objeto faz, em vez de como ele faz.

# Exemplo: Ao usar o método carro.acelerar(), você não precisa saber exatamente como o motor de combustão funciona; você só precisa saber que, ao chamar esse método, o carro ganha velocidade. A classe abstrai a complexidade do motor.

# Normalmente é alcançada pelo Encapsulamento (esconder detalhes) e pelo uso de Classes Abstratas (que definem uma estrutura obrigatória, mas não a implementam).

# Prática: Abstração via Interface (Classes Abstratas)

# Para garantir que classes filhas implementem um método específico, usamos o módulo abc (Abstract Base Classes).

from abc import ABC, abstractmethod

class FormaGeometrica(ABC): # Classe Abstrata
    @abstractmethod
    def calcular_area(self):
        # A classe pai não implementa, apenas exige que as filhas implementem
        pass 

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    # É obrigatório implementar este método
    def calcular_area(self): 
        return self.largura * self.altura

# Uso
r = Retangulo(5, 4)
print(f"A área do retângulo é: {r.calcular_area()}") 

# Se você tentasse instanciar a classe abstrata (FormaGeometrica()), daria erro.

# RESUMO
# Encapsulamento
#     Resumo: Agrupar dados e restringir acesso direto.
#     Benefício Principal: Proteção de dados e esconder detalhes.
    
# Herança
#     Resumo: Criar novas classes a partir de classes existentes.
#     Benefício Principal: Reutilização de código (Relação "É UM TIPO DE").
    
# Polimorfismo
#     Resumo: Um método se comporta de maneiras diferentes em classes diferentes.
#     Benefício Principal: Flexibilidade e código mais genérico.

# Abstração
#     Resumo: Mostrar apenas o essencial, escondendo a complexidade.
#     Benefício Principal: Simplificação do uso do objeto.
