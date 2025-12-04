class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0.0):
        self.titular = titular
        self._numero = numero
        self._saldo = saldo

    # Getters
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    def depositar(self, valor: float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor que 0.")
        
        self._saldo += valor

    def sacar(self, valor: float):
        if valor < 0:
            raise ValueError("O valor não pode ser menor que 0.")
            
        if self._saldo - valor < 0:
            raise ValueError("Você não pode sacar mais do que tem na conta.")
            
        self._saldo -= valor

    def transferir(self, valor: float, destino: "Conta"):
        self.sacar(valor)
        destino.depositar(valor)


conta1 = Conta('Davi', '12345', 100)
conta2 = Conta('Fernanda', '12544', 200)

# print('Conta de', conta1.titular, f'- R${conta1.saldo:.2f}')
# conta1.depositar(50)
# print('Conta de', conta1.titular, f'- R${conta1.saldo:.2f}')
# conta1.sacar(70)
# print('Conta de', conta1.titular, f'- R${conta1.saldo:.2f}')


print('Conta de', conta1.titular, f'- R${conta1.saldo:.2f}')
print('Conta de', conta2.titular, f'- R${conta2.saldo:.2f}')

conta2.transferir(70, conta1)

print('Conta de', conta1.titular, f'- R${conta1.saldo:.2f}')
print('Conta de', conta2.titular, f'- R${conta2.saldo:.2f}')
