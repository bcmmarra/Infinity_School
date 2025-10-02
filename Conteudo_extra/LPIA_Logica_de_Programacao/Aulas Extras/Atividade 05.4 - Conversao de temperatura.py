'''
Atividade 11 – Conversão de temperatura
Peça uma temperatura em graus Celsius e converta para Fahrenheit.
📌 Fórmula: F = C * 1.8 + 32
'''
print("--------| Conversor de Temperatura |--------")

print("----| Digite a temperatura em graus ºC |----")
t = float(input('Digite a temperatura atual em graus Celsius: '))
f = t * 1.8 + 32
print(f'A temperatura em graus Celsius é: {t:.2f}ºC')
print(f'A temperatura em graus Fahrenheit é: {f:.2f}ºF')

print("--| Digite a temperatura em graus ºF |--")
f = float(input('Digite a temperatura atual em graus F: '))
t = (f - 32) / 1.8
print(f'A temperatura em graus Fahrenheit é: {f:.2f}ºF')
print(f'A temperatura em graus Celsius é: {t:.2f}ºC')