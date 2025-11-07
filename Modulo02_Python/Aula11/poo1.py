# Definição da Classe
class Carro: 
    # Linha 1: 'class Carro:'
    # Define uma nova classe chamada 'Carro'. 
    # Uma classe é como um 'molde' ou 'planta' para criar objetos.
    
    # Metódo Construtor
    # O "self" deve ser o primeiro parametro nos metódos das Classes no Python
    def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: int) -> None:
        # Linha 2: 'def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: int) -> None:'
        # Define o *método construtor* da classe. O nome '__init__' (com dois underscores) é especial em Python 
        # e é chamado automaticamente quando um novo objeto é criado.
        # - 'self': É a referência obrigatória ao *próprio* objeto que está sendo criado.
        # - Os demais: São os parâmetros (dados) que precisamos fornecer para criar um carro. 
        #   As anotações ': str', ': int' e '-> None' são *type hints* que indicam os tipos esperados, 
        #   ajudando na clareza do código.
        
        self.marca = marca
        # Linha 3: 'self.marca = marca'
        # Cria um *atributo* (característica) chamado 'marca' para o objeto atual ('self').
        # O valor atribuído é o que foi passado no parâmetro 'marca'.
        
        self.modelo = modelo
        # Linha 4: 'self.modelo = modelo'
        # Cria o atributo 'modelo' e atribui o valor do parâmetro.
        
        self.ano = ano
        # Linha 5: 'self.ano = ano'
        # Cria o atributo 'ano' e atribui o valor do parâmetro.
        
        self.velocidade_maxima = velocidade_maxima
        # Linha 6: 'self.velocidade_maxima = velocidade_maxima'
        # Cria o atributo 'velocidade_maxima' e atribui o valor do parâmetro.
        
        self.velocidade_atual = 0 # Valor Inicial
        # Linha 7: 'self.velocidade_atual = 0'
        # Cria o atributo 'velocidade_atual'. 
        # Note que este valor *não* é passado como parâmetro; todo carro começa parado, então inicializamos com 0.

        # Sintaxe:
        # self.<atributo> = <valor>
        # O que vem depois do self é o nome do atributo

# --- Fim da definição da classe 'Carro' ---

carro1 = Carro("Honda", "Civic", 2020, 240)
# Linha 8: 'carro1 = Carro("Honda", "Civic", 2020, 240)'
# INSTANCIAÇÃO do objeto! Cria um novo objeto (instância) da classe 'Carro'.
# O método '__init__' é chamado internamente com os valores:
# - marca="Honda", modelo="Civic", ano=2020, velocidade_maxima=240.
# A variável 'carro1' armazena essa nova instância.

print("Carro 1: ")
# Linha 9: Imprime um cabeçalho.

print(f'Marca: {carro1.marca}') # 'Honda'
# Linha 10: Acessa e imprime o atributo 'marca' do objeto 'carro1'. Saída: 'Honda'.

print(f'Modelo: {carro1.modelo}') # 'Civic'
# Linha 11: Acessa e imprime o atributo 'modelo'. Saída: 'Civic'.

print(f'Ano Fabricação: {carro1.ano}') # 2020
# Linha 12: Acessa e imprime o atributo 'ano'. Saída: 2020.

print(f'Velocidade Máxima: {carro1.velocidade_maxima}') # 240
# Linha 13: Acessa e imprime o atributo 'velocidade_maxima'. Saída: 240.

print(f'Velocidade Atual: {carro1.velocidade_atual}') # 0
# Linha 14: Acessa e imprime o atributo 'velocidade_atual'. Saída: 0 (o valor inicial).

print("--------------------")
# Linha 15: Imprime uma linha separadora.

carro2 = Carro("Fiat", "Uno", 2023, 180)
# Linha 16: 'carro1 = Carro("Fiat", "Uno", 2023, 180)'
# Cria um *novo* objeto da classe 'Carro' com dados diferentes.
# IMPORTANTE: A variável 'carro1' *agora* armazena esta nova instância, 
# substituindo a referência ao objeto "Honda Civic" anterior (que é perdido da memória, se não houver outra referência).

print("Carro 2: ")
# Linha 17: Imprime o novo cabeçalho.

print(f'Marca: {carro2.marca}') # 'Fiat'
# Linha 18: Acessa e imprime o atributo 'marca' do *novo* objeto. Saída: 'Fiat'.

print(f'Modelo: {carro2.modelo}') # 'Uno'
# Linha 19: Acessa e imprime o atributo 'modelo' do *novo* objeto. Saída: 'Uno'.

print(f'Ano Fabricação: {carro2.ano}') # 2023
# Linha 20: Acessa e imprime o atributo 'ano' do *novo* objeto. Saída: 2023.

print(f'Velocidade Máxima: {carro2.velocidade_maxima}') # 180
# Linha 21: Acessa e imprime o atributo 'velocidade_maxima' do *novo* objeto. Saída: 180.

print(f'Velocidade Atual: {carro2.velocidade_atual}') # 0
# Linha 22: Acessa e imprime o atributo 'velocidade_atual' do *novo* objeto. Saída: 0.

# 📝 Resumo dos Conceitos
# Classe (class Carro): É o projeto, o molde, a definição de como um Carro deve ser.
# Objeto/Instância (carro1): É o item concreto criado a partir do molde. Cada objeto tem seus próprios valores para os atributos.
# Construtor (def __init__): É o método especial que garante que o objeto seja criado corretamente, inicializando todos os seus atributos (características).
# self: É a palavra-chave que permite que o objeto acesse a si mesmo e a seus atributos (self.marca). É fundamental.
# Atributos (self.marca, self.velocidade_atual): São as variáveis que armazenam as características do objeto (dados).
