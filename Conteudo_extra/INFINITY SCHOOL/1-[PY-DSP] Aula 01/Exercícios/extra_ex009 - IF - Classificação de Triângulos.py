'''
Exercício de Classificação de Triângulos:

"Faça um programa que classifique um triângulo com base nos comprimentos de seus três lados. Peça ao usuário para digitar os comprimentos dos lados (a, b, c) e imprima se o triângulo é:

Equilátero: Todos os três lados são iguais.

Isósceles: Apenas dois lados são iguais.

Escaleno: Todos os três lados são diferentes.

Validações Adicionais:

Verifique se os lados formam um triângulo válido: a soma de dois lados quaisquer deve ser maior que o terceiro lado (a + b > c, a + c > b, e b + c > a). Se não formarem um triângulo, imprima uma mensagem de erro."

Como você começaria a escrever o código para este desafio?
'''
a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))

# PRIMEIRO: Validação se os lados formam um triângulo válido
if (a + b > c) and (a + c > b) and (b + c > a):
    # Se formar um triângulo, então classificamos
    if a == b and b == c: # Equilátero: todos os lados são iguais
        print("O triângulo é Equilátero: Todos os três lados são iguais.")
    elif (a == b and a != c) or \
         (a == c and a != b) or \
         (b == c and b != a): # Isósceles: apenas dois lados são iguais
        print("O triângulo é Isósceles: Apenas dois lados são iguais.")
    else: # Escaleno: todos os lados são diferentes
        print("O triângulo é Escaleno: Todos os três lados são diferentes.")
else:
    # Se a condição de validação inicial não for atendida
    print("Os lados digitados NÃO formam um triângulo válido!")

print("---- FIM - Classificador de Triângulos ----")


# A barra invertida \ no final de uma linha em Python (or \) é um operador de continuação de linha.

# Por que usar or \ em linhas diferentes?
# Legibilidade (Melhoria na Leitura):

# Sua condição para identificar um triângulo Isósceles é bastante longa e detalhada: (a == b and a != c) or (a == c and a != b) or (b == c and b != a).

# Se você colocasse tudo em uma única linha, ela ficaria muito extensa e difícil de ler, especialmente em telas menores ou com muitas janelas abertas.

# Ao usar \, você pode "quebrar" a linha em pontos lógicos (como após um operador or), tornando o código mais organizado e fácil de entender visualmente. Cada parte da condição fica em sua própria linha, o que facilita a identificação das diferentes possibilidades para um triângulo Isósceles.

# Continuação de Instrução:

# O \ informa ao interpretador Python que a instrução atual (neste caso, a condição elif) continua na próxima linha. Sem ele, o Python assumiria que a linha terminou após o or e geraria um erro de sintaxe.

# Exemplo (Comparação):
# Sem a continuação de linha (difícil de ler):

# Python

# elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
#     print("O triângulo é Isósceles...")
# Com a continuação de linha (mais legível):

# Python

# elif (a == b and a != c) or \
#      (a == c and a != b) or \
#      (b == c and b != a):
#      print("O triângulo é Isósceles...")
# Observação sobre Parênteses:
# É importante notar que, em Python, quando você tem uma instrução contida dentro de parênteses (), colchetes [] ou chaves {} (como o ( e ) que envolvem toda a sua condição elif), a continuação de linha é implícita. Ou seja, você poderia ter quebrado as linhas sem a barra invertida nesse caso específico, e o Python ainda entenderia.

# No entanto, usar a barra invertida \ é uma prática comum e explícita para indicar que a linha continua, o que muitos programadores preferem para clareza em condições complexas como a sua.
