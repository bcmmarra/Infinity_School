from dataclasses import dataclass

@dataclass
class Conta:
    titulo: str
    numero: str
    saldo: float

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


conta1 = Conta('Davi', '12345', 100)
print(conta1)

print(conta1.saldo)
