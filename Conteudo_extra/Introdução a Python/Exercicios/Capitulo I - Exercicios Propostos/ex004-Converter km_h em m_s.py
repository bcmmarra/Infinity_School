'''
4. Implemente um programa que converta o valor de uma velocidade
média em km/h para m/s. Para isso, o usuário deve
informar o valor da velocidade média. Sabe-se que o fator utilizado
para essa conversão é 3,6.
'''

print("--- Converter Km/h para m/s ---")
km = float(input("Digite a velocidade média (Km/h): "))
mt = km / 3.6

mt = float(input("Digite a velocidade média (ms/s): "))
km = mt * 3.6

print(f"A velocidade média em m/s é {mt}")
print(f"A velocidade média em Km/h é {km}")
print("---------------------------------------------------")