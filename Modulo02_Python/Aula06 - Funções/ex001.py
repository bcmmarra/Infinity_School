# ## Atividade 1

# Crie uma função chamada `calcular_area_retangulo` que:

# - Receba dois parâmetros: `largura` e `altura` (ambos do tipo `float`).
# - Retorne a área do retângulo (também um `float`).
# - Utilize **type hints** nos parâmetros e no retorno da função.

# 📌 **Exemplo esperado:**
# area = calcular_area_retangulo(5.0, 3.0)
# print(area)  # 15.0

def calcular_area_retangulo(largura: float, altura: float) -> float:
    return largura * altura


largura = float(input('Digite a Largura: '))
altura = float(input('Digite a altura: '))

area = calcular_area_retangulo(largura, altura)
print(f'A area total é: {area:.2f}')
