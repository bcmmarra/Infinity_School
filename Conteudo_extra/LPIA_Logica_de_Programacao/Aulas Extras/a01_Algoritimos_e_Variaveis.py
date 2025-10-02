# 🔹 1. Introdução à Lógica de Programação
# ✔ O que é Lógica de Programação?
# É a habilidade de resolver problemas de forma organizada, dividindo tarefas complexas em etapas simples e executáveis.

# 📌 Exemplo real: Fazer um suco de laranja.
# Etapas lógicas:

# 1 - Pegar as laranjas
# 2 - Cortar
# 3 - Espremer
# 4 - Coar
# 5 - Servir

# 🔍 Objetivo: aprender a pensar como um computador, ou seja, de forma sequencial e lógica.

# 🔹 2. Algoritmo
# ✔ O que é?
# É uma sequência finita de instruções claras e ordenadas, feitas para resolver um problema.

# ✔ Por que é importante?
# Organiza soluções
# Permite reuso de código
# Melhora a eficiência
# Facilita a leitura e manutenção

# 📌 Exemplo: Criar um algoritmo para fazer chá.
# Etapas:

# 1 - Ferver água
# 2 - Colocar o chá na xícara
# 3 - Despejar a água
# 4 - Esperar alguns minutos
# 5 - Beber

# 🔹 3. Diferença entre Lógica e Algoritmo
# Lógica ------------------|------ Algoritmo
# Planejamento-------------|------ Execução prática
# Raciocínio estruturado---|------ Instruções claras
# Resolução de problemas---|------ Passos para solução
# ✔ Lógica é o raciocínio por trás da solução, enquanto algoritmo é a forma escrita dessa solução.

# Pensar na Solução
# ✔ Como pensar na solução?
# 1. Entender o problema
# 2. Dividir em partes menores
# 3. Organizar as etapas
# 4. Escrever os passos

# ✔ Exemplo: Fazer um bolo
# 1. Entender o problema: Fazer um bolo de chocolate
# 2. Dividir em partes menores: Ingredientes, preparo, assar
# 3. Organizar as etapas: Misturar ingredientes, colocar na forma, assar
# 4. Escrever os passos:
#   - Pegar os ingredientes
#   - Misturar farinha, açúcar, ovos e chocolate
#   - Colocar na forma
#   - Assar por 30 minutos
#   - Deixar esfriar

# 🔹 4. Conhecendo o VSCode e Python
# ✔ VSCode
# Editor de código leve, gratuito e poderoso.

# ✔ Python
# Linguagem simples e muito usada para desenvolvimento web, automações, ciência de dados, etc.

# ✔ Instalação Básica
# Baixar Python do site oficial
# Baixar VSCode do site oficial
# Instalar extensão Python, Pylance e Python Debugger no VSCode

# 🔹 5. Variáveis
# ✔ O que é?
# Um espaço na memória para armazenar dados. Pode mudar de valor ao longo do tempo.

# 📌 Sintaxe:
mensagem = "Olá, mundo!"

# ✔ Tipos de Variáveis:
# str (string) → textos: "Carlos"
# int (inteiro) → números sem ponto: 30
# float (ponto flutuante) → números com ponto: 1.85
# bool (booleano) → verdadeiro ou falso: True ou False

# 📌 Exemplo:
nome = "Ana"
idade = 25
altura = 1.65
maior_de_idade = True

# 🔹 6. Funções Internas do Python
# ✔ print()
# Mostra informações na tela.
print("Olá, mundo!")

# ✔ type()
# Mostra o tipo da variável.
print(type(25))     # int
print(type("25"))   # str
print(type(1.5))    # float

# ✔ input()
# Recebe algo digitado pelo usuário (sempre retorna uma string).
nome = input("Digite seu nome: ")

# 🔹 7. Atividades Práticas
# ✔ Atividade 01:
saudacao = "Hello World"
print(saudacao)

# ✔ Atividade 02:
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))

# 🔹 8. Operadores Aritméticos
# ✔ O que são?
# São símbolos que realizam operações matemáticas básicas.

# 📌 Tabela de Operadores Aritméticos:
# | Operador | Descrição          | Exemplo  | Resultado |
# |----------|--------------------|----------|-----------|
# | +        | Soma               | 3 + 2    | 5         |
# | -        | Subtração          | 3 - 2    | 1         |
# | *        | Multiplicação      | 3 * 2    | 6         |
# | /        | Divisão            | 3 / 2    | 1.5       |
# | %        | Módulo             | 3 % 2    | 1         |
# | **       | Potência           | 3 ** 2   | 9         |
# | //       | Divisão inteira    | 3 // 2   | 1         |
# ✔ Operadores Aritméticos são usados para realizar cálulos matemáticos básicos.

# 🔹 Exemplos de Operadores Aritméticos
# ✔ Soma: +
# Adiciona dois números.
a = 10
b = 5
print(a + b)  # Resultado: 15

# ✔ Subtração: -
# Subtrai o segundo número do primeiro.
a = 10
b = 5
print(a - b)  # Resultado: 5

# ✔ Multiplicação: *
# Multiplica dois números.
a = 10
b = 5
print(a * b)  # Resultado: 50

# ✔ Divisão: /
# Divide o primeiro número pelo segundo.
a = 10
b = 5
print(a / b)  # Resultado: 2.0

# ✔ Divisão Inteira: //
# Divide o primeiro número pelo segundo e retorna apenas a parte inteira.
a = 10
b = 3
print(a // b)  # Resultado: 3

# ✔ Módulo: %
# Retorna o resto da divisão do primeiro número pelo segundo.
a = 10
b = 3
print(a % b)  # Resultado: 1

# ✔ Potência: **
# Eleva o primeiro número à potência do segundo.
a = 2
b = 3
print(a ** b)  # Resultado: 2 * 2 * 2 = 8

# ✔ Ordem de Precedência:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*) e Divisão (/)
# 4. Adição (+) e Subtração (-)

# A ordem de precedência determina a sequência em que as operações são realizadas.
# 🔹 Exemplo 1  de Ordem de Precedência:
# Vamos considerar a expressão: a + b * c
# Vamos considerar a expressão: (a + b) * c
# Onde:
a = 10
b = 5
c = 2
resultado = a + b * c   # Multiplicação é feita antes da adição
print(resultado)        # Resultado: 20 (5 * 2 = 10, depois 10 + 10 = 20)

resultado1 = a + b * c      # Multiplicação antes da soma: 10 + (5 * 2) = 20
resultado2 = (a + b) * c    # Parênteses primeiro: (10 + 5) * 2 = 30

print("Sem parênteses:", resultado1)   # Saída: 20
print("Com parênteses:", resultado2)   # Saída: 30

# 🔹 Exemplo 2 de Ordem de Precedência:
# Vamos considerar a expressão: a + b * c - d / e
# Onde:
a = 10
b = 5
c = 2
d = 8
e = 4
resultado = a + b * c - d / e   # Multiplicação e divisão antes da adição e subtração
print(resultado)                # Resultado: 10 + (5 * 2) - (8 / 4) = 10 + 10 - 2 = 18
                                
                                # 1. Multiplicação: b * c = 5 * 2 = 10
                                # 2. Divisão: d / e = 8 / 4 = 2
                                # 3. Soma: a + (resultado da multiplicação) = 10 + 10 = 20
                                # 4. Subtração: (resultado da soma) - (resultado da divisão) = 20 - 2 = 18

# 🔹 8.1. Operadores de Atribuição  
# ✔ O que são?
# São usados para atribuir valores a variáveis, podendo também realizar operações ao mesmo tempo.
# 📌 Tabela de Operadores de Atribuição:
# | Operador | Descrição                     | Exemplo     | Resultado  |
# |----------|-------------------------------|-------------|------------|
# | =        | Atribuição simples            | x = 5       | x = 5      |
# | +=       | Adiciona e atribui            | x += 3      | x = x + 3  |
# | -=       | Subtrai e atribui             | x -= 2      | x = x - 2  |
# | *=       | Multiplica e atribui          | x *= 4      | x = x * 4  |
# | /=       | Divide e atribui              | x /= 2      | x = x / 2  |
# | %=       | Módulo e atribui              | x %= 3      | x = x % 3  |
# | //=      | Divisão inteira e atribui     | x //= 2     | x = x // 2 |
# | **=      | Potência e atribui            | x **= 2     | x = x ** 2 |
# ✔ Exemplo de Uso:
x = 10
x += 5  # x agora é 15
x -= 3  # x agora é 12
x *= 2  # x agora é 24
x /= 4  # x agora é 6.0
x %= 5  # x agora é 1.0
x //= 2 # x agora é 0.0
x **= 3 # x agora é 0.0

# 🔹 8.2. Operadores de Comparação
# ✔ O que são?
# São usados para comparar valores, retornando True ou False.
# 📌 Tabela de Operadores de Comparação:
# | Operador | Descrição                     | Exemplo     | Resultado |
# |----------|-------------------------------|-------------|-----------|
# | ==       | Igualdade                     | x == y      | True/False|
# | !=       | Diferença                     | x != y      | True/False|
# | >        | Maior que                     | x > y       | True/False|
# | <        | Menor que                     | x < y       | True/False|
# | >=       | Maior ou igual a              | x >= y      | True/False|
# | <=       | Menor ou igual a              | x <= y      | True/False|
# ✔ Exemplo de Uso:
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# 🔹 8.3. Operadores Lógicos
# ✔ O que são?
# São usados para combinar expressões booleanas, retornando True ou False.
# 📌 Tabela de Operadores Lógicos:
# | Operador | Descrição                             | Exemplo     | Resultado |
# |----------|---------------------------------------|-------------|-----------|
# | and      | Verdadeiro se ambos forem True        | x and y     | True/False|
# | or       | Verdadeiro se pelo menos um for True  | x or y      | True/False|
# | not      | Inverte o valor booleano              | not x       | True/False|
# ✔ Exemplo de Uso:
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
print(not y)    # True

# 🔹 8.4. Operadores de Identidade
# ✔ O que são?
# São usados para verificar se duas variáveis referenciam o mesmo objeto na memória.
# 📌 Tabela de Operadores de Identidade:
# | Operador | Descrição                               | Exemplo     | Resultado |
# |----------|-----------------------------------------|-------------|-----------|
# | is       | Verdadeiro se forem o mesmo objeto      | x is y      | True/False|
# | is not   | Verdadeiro se não forem o mesmo objeto  | x is not y  | True/False|
# ✔ Exemplo de Uso:
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)        # True (mesmo objeto)
print(x is z)        # False (objetos diferentes)
print(x is not z)    # True (objetos diferentes)

# 🔹 8.5. Operadores de Membro
# ✔ O que são?
# São usados para verificar se um valor está presente em uma sequência (como listas, tuplas ou strings).

# 📌 Tabela de Operadores de Membro:
# | Operador | Descrição                                      | Exemplo     | Resultado |
# |----------|------------------------------------------------|-------------|-----------|
# | in       | Verdadeiro se o valor estiver na sequência     | x in y      | True/False|
# | not in   | Verdadeiro se o valor não estiver na sequência | x not in y  | True/False|
# ✔ Exemplo de Uso:
lista = [1, 2, 3, 4, 5]
print(3 in lista)        # True
print(6 in lista)        # False
print(3 not in lista)    # False
print(6 not in lista)    # True

# 🔹 9. F-Strings ou formatted
# ✔ O que são?
# F-strings são uma forma moderna e eficiente de formatar strings em Python, permitindo a inclusão de variáveis diretamente dentro de strings. 

# 📌 Sintaxe:
nome = "João"
idade = 20
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# ✔ Vantagens:
# - Mais legível e fácil de entender
# - Rápida e flexível
# - Permite incluir expressões diretamente na string
# print(f"Em 10 anos terei {idade + 10} anos.")
# 🔹 Exemplo de Uso:
# Vamos considerar a seguinte situação:
# Você quer apresentar informações sobre uma pessoa, como nome, idade e cidade natal.
# Você pode usar f-strings para formatar essa informação de forma clara e concisa.
# Exemplo:
nome = "Maria"
idade = 30
cidade = "São Paulo"
print(f"{nome} tem {idade} anos e é de {cidade}.")

nome = "João"
idade = 20
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")


# 🔹 10. Projetos Práticos
# ✔ Projeto 01 - Média de Notas:
# Objetivo: Criar um Programa que Peça as 4 Notas Bimestrais e Mostre a Média

# # Solicita as notas do usuário e calcula a média de quatro notas, exibindo o resultado formatado.
# 1 - Solicita as notas do usuário
# Use a função inpu() para pedir ao usuário que insira suas quatro notas. Converta as entradas do usuário de string para números (float) para permitir cálculos.

# 2 - Calcular a Média das Notas
# Some as quatro notas e divida o resultado por 4 para obter a média.

# 3 - Mostrar a Média Calculada para o Usuário
# Use a função print() para exibir a média formatada com duas casas decimais.

#----------------------------------------------------------------------------------------------------

# ✔ Projeto 02 - Cálculo de Salário por Hora
# Objetivo: Criar um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, calcule o salário total e exiba o resultado (considere que você trabalha 20 dias no mês).

# 1 - Solicitar o Salário Mensal:
# Use a função input() para pedir ao usuário que insira quanto ele ganha por mês. Converta a entrada do usuário de string para um número (float) para permitir cálculos.

# 2 - Solicitar o Número de Horas Trabalhadas por Semana:
# Use a função input() para pedir ao usuário que insira o número de horas ele trabalhadas na semana. Converta essa entrada também para (float) para permitir cálculos.

# 3 - Calcular o Número de Horas Trabalhadas no Mês:
# Multiplique o número de horas trabalhadas por semana por 4 (considerando 4 semanas no mês) para obter o total de horas trabalhadas no mês.

# 4 - Calcular o Valor da Hora Trabalhada:
# Divida o salário mensal pelo total de horas trabalhadas no mês para obter o valor da hora trabalhada.

# 5 - Exibir o Resultado:
# Use a função print() para exibir o valor da hora trabalhada formatado com duas casas decimais.

#----------------------------------------------------------------------------------------------------
# ✔ Projeto 03 - Dados Pessoais
# Objetivo: Criar um Programa que Pergunte o Nome, Idade e Cidade Natal do Usuário e Exiba uma Mensagem Personalizada

# 1 - Solicitar o Nome do Usuário:
# Use a função input() para pedir ao usuário que insira seu nome. A entrada será uma string.

# 2 - Solicitar a Idade do Usuário:
# Use a função input() para pedir ao usuário que insira sua idade. Converta a entrada do usuário de string para um número inteiro (int) para permitir cálculos ou comparações futuras.

# 3 - Solicitar a Cidade Natal do Usuário:
# Use a função input() para pedir ao usuário que insira sua cidade natal. A entrada será uma string.

# 4 - Exibir uma Mensagem Personalizada:
# Use a função print() para exibir uma mensagem personalizada que inclua o nome, idade e cidade natal do usuário. Você pode usar f-strings para facilitar a formatação da mensagem.

# 🔹 11. Conclusão
# ✔ Resumo do que foi aprendido:
# - Lógica de Programação: Pensar de forma organizada e sequencial.
# - Algoritmos: Criar sequências de passos para resolver problemas.
# - Variáveis: Armazenar dados e trabalhar com diferentes tipos.
# - Operadores: Realizar cálculos e comparações.
# - F-strings: Formatar strings de forma eficiente.
# - Projetos Práticos: Aplicar o conhecimento em situações reais.
# ✔ Próximos passos:
# - Praticar mais com exercícios e projetos.