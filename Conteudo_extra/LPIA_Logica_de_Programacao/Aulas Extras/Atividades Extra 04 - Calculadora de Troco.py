'''
🔹 Exercício 4 – Calculadora de Troco
Peça:

O valor total da compra
O valor pago pelo cliente

Mostre o troco usando f-string, como:
Troco: R$ 13.25
'''

valor_compra = float(input("Digite o valor total da compra: R$ "))
valor_pago  = float(input("Digite o valor total pago: R$ "))

troco = valor_pago - valor_compra

print(f"Troco: R$ {troco:.2f}.")

# Resolução
valor_compra = float(input("Valor da compra: "))
valor_pago = float(input("Valor pago: "))
troco = valor_pago - valor_compra

print(f"Troco: R$ {troco:.2f}")
