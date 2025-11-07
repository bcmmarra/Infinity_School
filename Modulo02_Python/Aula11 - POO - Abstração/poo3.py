class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    # Metódo Acelerar
    # O "self" sempre como primeiro parametro do metódo
    # Portanto os parametros reais da função são posicionados depois do "self"
    def acelerar(self, velocidade: int) -> int:
        self.velocidade_atual += velocidade
        return self.velocidade_atual

    # Metódo Frear
    # O "self" sempre como primeiro parametro do metódo
    def frear(self, velocidade: int) -> int:
        self.velocidade_atual -= velocidade
        return self.velocidade_atual


# Criando 1º Carro
carro1 = Carro("Honda", "Civic", 2020, 240)

while True:
    print(carro1)
    print(f'Ano: {carro1.ano}')
    print(f'Velocidade Máxima: {carro1.velocidade_maxima}')

    action = input('-> [A]celerar / [F]rear / [S]air: ')

    if action == "S":
        break

    velocidade = int(input('Digite a velocidade de aceleração ou freio: '))

    if action == "A":
        carro1.acelerar(velocidade)
    
    elif action == "F":
        carro1.frear(velocidade)

    else:
        print('Opção inválida')  
