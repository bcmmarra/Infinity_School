'''
🔹 Exercício 7 – Somando palavras numéricas
Peça dois números ao usuário como texto (input()), mas sem converter.
Depois, use int() para somá-los corretamente.

📌 Dica:
"4" + "5" = "45" (string)  
int("4") + int("5") = 9 (int)
'''

n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

soma = int(n1) + int(n2)

print (f"{n1} + {n2} = {n1+n2} (string - Concatenação)")
print (f"{n1} + {n2} = {soma} (int - Conversão string => numero)")

# Resolução
a = input("Digite um número: ")
b = input("Digite outro número: ")

print("Sem conversão:", a + b)  # concatenação
print("Com conversão:", int(a) + int(b))  # soma real
