# A coesão da classe Carro é alta, pois seus métodos (acelerar, frear)
# e atributos (velocidade, modelo, etc.) estão focados em uma única responsabilidade:
# gerenciar o estado e comportamento de um carro.

class Carro:
    # Método Construtor (__init__)
    # Este método é chamado automaticamente ao criar uma nova instância (objeto).
    # 'self' é a referência à instância que está sendo criada.
    def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: int) -> None:
        # Atributos de identificação e limite (passados como parâmetros)
        self.marca = marca                # Atribui a marca
        self.modelo = modelo              # Atribui o modelo
        self.ano = ano                    # Atribui o ano
        self.velocidade_maxima = velocidade_maxima # Atribui a velocidade máxima

        # Atributo de estado inicial (definido internamente)
        # Todo carro inicia com velocidade zero. Este é o estado interno que será alterado pelos métodos.
        self.velocidade_atual = 0

    # Metódo Acelerar
    # O 'self' é sempre o primeiro parâmetro, referenciando o objeto em que o método é chamado.
    # 'velocidade' é o valor a ser adicionado à velocidade atual.
    def acelerar(self, velocidade: int) -> int:
        # Lógica da Ação: Modifica o estado interno da instância.
        # Adiciona o valor de 'velocidade' ao atributo 'self.velocidade_atual'.
        self.velocidade_atual += velocidade
        
        # Retorna o novo valor da velocidade atual após a aceleração.
        return self.velocidade_atual

    # Metódo Frear
    # O 'self' é sempre o primeiro parâmetro, referenciando o objeto.
    def frear(self, velocidade: int) -> int:
        # Lógica da Ação: Modifica o estado interno da instância.
        # Subtrai o valor de 'velocidade' do atributo 'self.velocidade_atual'.
        self.velocidade_atual -= velocidade
        
        # Retorna o novo valor da velocidade atual após a frenagem.
        return self.velocidade_atual
    
    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} ({self.ano}) | Velocidade Atual: {self.velocidade_atual} km/h"
# --- Demonstração de Uso da Classe ---

# Criando 1º Carro
# Instancia um objeto 'carro1', chamando o construtor (__init__) com os valores fornecidos.
carro1 = Carro("Honda", "Civic", 2020, 240)
print(carro1)

# Acessando Atributos
# Acessa e imprime o atributo 'modelo' do objeto 'carro1'.
print(f'Carro: {carro1.modelo}')
# Acessa e imprime o atributo 'velocidade_atual', que foi inicializado em 0 pelo construtor.
print(f'Velocidade Atual: {carro1.velocidade_atual}')  # Saída: 'Velocidade Atual: 0'

# Chamando o metódo acelerar
# Chama o método 'acelerar' no objeto 'carro1', passando 20.
# O estado interno 'carro1.velocidade_atual' muda de 0 para 20.
carro1.acelerar(20)
# Verifica o novo estado após a aceleração.
print(f'Velocidade Atual: {carro1.velocidade_atual}')  # Saída: 'Velocidade Atual: 20'

# Chamando o metódo frear
# Chama o método 'frear' no objeto 'carro1', passando 5.
# O estado interno 'carro1.velocidade_atual' muda de 20 para 15.
carro1.frear(5)
# Verifica o estado final após a frenagem.
print(f'Velocidade Atual: {carro1.velocidade_atual}')  # Saída: 'Velocidade Atual: 15'