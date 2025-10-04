# Crie uma função chamada calcular_imc que recebe o peso e a altura e retorna o imc
# fórmula do IMC (Índice de Massa Corporal) é: IMC = peso (kg) ÷ (altura (m) x altura (m)).

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

print(calcular_imc(peso=76.8, altura=1.71))
# Saída: 26.26449163845286

