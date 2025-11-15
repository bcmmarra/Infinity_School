# Sistema Básico de Gerenciamento de Biblioteca

# Nosso sistema terá duas classes principais:
#   ItemBiblioteca (abstrata, para definir a estrutura básica de qualquer item)
#   Livro (que herda e implementa essa estrutura).

# Passo 1: Abstração (Classe Abstrata) e Encapsulamento
# Vamos criar a classe base ItemBiblioteca. Ela será abstrata para garantir que qualquer coisa que seja um item da biblioteca (livro, revista, DVD) tenha um título e um método para exibir detalhes.

# Importação
from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    """Classe base abstrata para todos os itens da biblioteca."""
    
    def __init__(self, titulo, ano_publicacao):
        # Atributos "Protegidos" (Encapsulamento)
        self._titulo = titulo
        self._ano = ano_publicacao
        self._emprestado = False # Encapsulamento de estado

    # Método Abstrato: Deve ser implementado por todas as subclasses (Abstração)
    @abstractmethod
    def exibir_detalhes(self):
        """Método que deve ser implementado para mostrar detalhes específicos do item."""
        pass
    
    # Getter para o título (Encapsulamento)
    @property
    def titulo(self):
        return self._titulo
    
    # Métodos de controle de estado (Comportamento)
    def emprestar(self):
        if not self._emprestado:
            self._emprestado = True
            print(f"'{self._titulo}' emprestado com sucesso.")
        else:
            print(f"'{self._titulo}' já está emprestado.")
            
    def devolver(self):
        if self._emprestado:
            self._emprestado = False
            print(f"'{self._titulo}' devolvido com sucesso.")
        else:
            print(f"'{self._titulo}' não estava emprestado.")

# Passo 2: Herança e Sobrescrita
# Agora criaremos a classe Livro, que herda todos os atributos e métodos de ItemBiblioteca.

class Livro(ItemBiblioteca):
    """Representa um livro específico na biblioteca."""
    
    def __init__(self, titulo, ano_publicacao, autor, num_paginas):
        # Herança: Chama o construtor da classe pai para inicializar atributos
        super().__init__(titulo, ano_publicacao)
        self._autor = autor
        self._num_paginas = num_paginas
        
    # Polimorfismo / Sobrescrita: Implementa o método abstrato exigido pela classe pai
    def exibir_detalhes(self):
        status = "Emprestado" if self._emprestado else "Disponível"
        print(f"\n--- Detalhes do Livro ---")
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Ano: {self._ano}")
        print(f"Páginas: {self._num_paginas}")
        print(f"Status: {status}")

# Passo 3: Polimorfismo (Prática de Uso)
# Vamos criar um segundo tipo de item, a Revista, que também herda de ItemBiblioteca e implementa seu próprio método exibir_detalhes.

class Revista(ItemBiblioteca):
    """Representa uma revista na biblioteca."""
    
    def __init__(self, titulo, ano_publicacao, edicao, mes):
        super().__init__(titulo, ano_publicacao)
        self._edicao = edicao
        self._mes = mes
    
    # Polimorfismo / Sobrescrita: Implementa o método abstrato
    def exibir_detalhes(self):
        status = "Emprestada" if self._emprestado else "Disponível"
        print(f"\n--- Detalhes da Revista ---")
        print(f"Título: {self._titulo}")
        print(f"Edição: {self._edicao} ({self._mes})")
        print(f"Ano: {self._ano}")
        print(f"Status: {status}")

# Função polimórfica que aceita qualquer objeto ItemBiblioteca
def processar_item(item):
    """Função que demonstra o polimorfismo ao tratar diferentes tipos de itens."""
    print(f"\nProcessando item: {item.titulo}")
    item.exibir_detalhes() # Chama o método específico da classe do objeto
    item.emprestar()      # Chama o método herdado da classe base
    

# Passo 4: Execução e Teste
# Vamos criar objetos e testar todas as funcionalidades.

# 1. Instanciação de Objetos
livro1 = Livro("Pilha de POO", 2023, "Prof. Gemini", 450)
revista1 = Revista("Python Mensal", 2024, "Ed. 55", "Maio")

# 2. Testando o Encapsulamento e Comportamento
print("\n--- Teste de Encapsulamento e Estado ---")
livro1.emprestar()  # Empresta o livro
livro1.emprestar()  # Tenta emprestar novamente (deve mostrar a mensagem "já está emprestado")
# print(livro1._emprestado) # Desencorajado: Acessando atributo protegido diretamente
livro1.devolver()   # Devolve o livro

# 3. Testando Herança e Polimorfismo
print("\n--- Teste de Herança e Polimorfismo ---")

# O loop trata Livro e Revista usando o mesmo código (Polimorfismo)
itens = [livro1, revista1] 

for item in itens:
    # A função processar_item chama o método correto de cada objeto
    processar_item(item)
    
# Visualmente, você pode imaginar o diagrama de classes aqui:
# ItemBiblioteca -> Livro e ItemBiblioteca -> Revista


# Mostrando o estado final dos itens
print("\n--- Estado Final ---")
livro1.exibir_detalhes()
revista1.exibir_detalhes()


# ====================================================

# Resumo do que foi Aplicado:
# Abstração: A classe ItemBiblioteca define a interface (exibir_detalhes) que todos os itens devem seguir, escondendo a implementação.

# Encapsulamento: Os atributos internos (_titulo, _emprestado) são protegidos e só são alterados por métodos de controle (emprestar, devolver).

# Herança: Livro e Revista herdam a lógica de empréstimo e devolução da classe ItemBiblioteca.

# Polimorfismo: A função processar_item e o loop for chamam item.exibir_detalhes(), e o Python executa a versão correta do método, seja ela de Livro ou de Revista.