# ## Atividade 2

# Crie uma função chamada `calcular_media` que:

# - Receba uma lista de números (do tipo `list[float]`).
# - Retorne a média desses números (do tipo `float`).
# - Utilize **type hints** nos parâmetros e no retorno da função.

# 📌 **Exemplo esperado:**
# media = calcular_media([7.5, 8.0, 9.0])
# print(media)  # 8.166...

def calcular_media (notas: list[float]) -> float:
    return sum(notas) / len(notas)

notas: list[float] = []

for n in range(3):
    nota = float(input(f'Digite a {n+1}º nota: '))
    notas.append(nota)

media = calcular_media(notas)

print(media)
