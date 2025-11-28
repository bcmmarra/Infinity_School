class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor que 0.")
        
        self.saldo += valor

    def sacar(self, valor: float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor que 0.")
            
        if self.saldo - valor < 0:
            raise ValueError("Você não pode sacar mais do que tem na conta.")
            
        self.saldo -= valor

    def transferir(self, valor: float, destino: "Conta"):
        self.sacar(valor)
        destino.depositar(valor)

    def __str__(self):
        return f'{self.titular} (R${self.saldo:.2f})'


conta1 = Conta('Davi', '0000-1', 100)

print(conta1)
conta1.sacar(20)
print(conta1)

conta2 = Conta('Fernanda', '1111-0', 100)

print(conta2)
conta2.transferir(50, conta1)

print(conta1)
print(conta2)