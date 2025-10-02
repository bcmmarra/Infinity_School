'''"AULA 01 | Python - PY - Revisão Lógica"

---------------- Seção 1. Operadores de comparação & operadores Lógicos ----------------

Seção 1. Introdução ao Controle de Fluxo
Controle de fluxo é a capacidade de ajustar a maneira como um programa executa suas tarefas.

É a habilidade de ajustar a maneira como um programa realiza suas tarefas."
Isso significa que você pode determinar a ordem em que as instruções do seu código serão executadas.

Através de instruções especiais, chamadas comandos, essas tarefas podem ser executadas seletivamente, repetidamente ou excepcionalmente.

Existem três tipos diferentes de estruturas de controle de fluxo: estruturas sequenciais, estruturas de decisão e estruturas de repetição.

- Estruturas sequenciais: Ações executadas uma após a outra, na ordem em que aparecem no código.
- Estruturas de decisão (ou condicionais): Permitem que o programa tome decisões e execute blocos de código diferentes com base em certas condições.
- Estruturas de repetição (ou laços): Permitem que um bloco de código seja executado várias vezes. '''

'''Exemplos:
1. Estruturas Sequenciais
Uma estrutura sequencial é a mais básica. As instruções são executadas em ordem, uma após a outra, exatamente como aparecem no código.'''

# 1. Primeira instrução
print("Olá!") 

# 2. Segunda instrução
nome = input("Qual é o seu nome? ")

# 3. Terceira instrução
print("Prazer em te conhecer,", nome) 

'''Neste exemplo:
Primeiro, a mensagem "Olá!" é impressa.
Em seguida, o programa pede o nome do usuário e armazena na variável nome.
Por último, ele imprime uma mensagem de cumprimento usando o nome que foi digitado.
As ações acontecem em uma sequência definida.

Olá!
Qual é o seu nome? Bruno
Prazer em te conhecer, Bruno'''

'''2. Estruturas de Decisão (ou Condicionais)
As estruturas condicionais permitem que o programa execute blocos de código diferentes com base em uma condição ser verdadeira ou falsa. As principais são if, else e elif. '''

idade = int(input("Qual é a sua idade? "))

if idade >= 18: # Condição: idade é maior ou igual a 18?
    print("Você é maior de idade.")
else: # Se a condição acima for falsa
    print("Você é menor de idade.")

'''Neste caso:
Se a idade digitada for 18 ou mais, a primeira mensagem será impressa.
Caso contrário (se a idade for menor que 18), a segunda mensagem será impressa.
Qual é a sua idade? 33
Você é maior de idade.'''

'''elif para quando precisamos de mais de 2 resultados (condições). Um exemplo dado é o de um semáforo.
Exemplo em Python (usando if, elif, else):'''

cor_semaforo = "amarelo"

if cor_semaforo == "verde":
    print("Acelerar!")
elif cor_semaforo == "amarelo":
    print("Atenção!")
else:
    print("Parar!")

'''Aqui, o programa verifica a cor do semáforo e imprime a instrução correspondente. 
Atenção!

3. Estruturas de Repetição (ou Laços)
As estruturas de repetição permitem que um bloco de código seja executado várias vezes, até que uma determinada condição seja satisfeita.  As mais comuns são for e while.

O for é frequentemente usado para iterar sobre uma sequência (como uma lista, string ou range de números). '''

# As estruturas de repetição, também conhecidas como loops ou laços, são uma das ferramentas mais poderosas na programação. Elas permitem que você execute um bloco de código repetidamente, sem ter que escrever o mesmo código várias vezes. Isso é fundamental para automação e para processar grandes volumes de dados.

# O for loop é um tipo de laço de repetição usado principalmente para iterar sobre uma sequência (como uma lista de itens, os caracteres de uma string ou uma faixa de números) ou para executar um bloco de código um número fixo de vezes.

# Componentes de um for loop:
# A palavra-chave for: Indica o início do laço de repetição.

# Variável de Iteração: Uma variável (você pode dar o nome que quiser, como item, i, numero, etc.) que assume o valor de cada elemento da sequência a cada repetição do loop.

# A palavra-chave in: Conecta a variável de iteração com a sequência.

# Sequência/Iterável: O conjunto de itens sobre o qual o loop irá iterar. Pode ser uma lista, uma string, uma tupla ou, muito comumente, uma range().

# Corpo do Loop: O bloco de código indentado que será executado em cada repetição.

# Sintaxe Básica:

# for variavel_de_iteracao in sequencia:
#     # Código a ser repetido
#     # Este código será executado para cada item na sequência

# Exemplos Comuns:

# Exemplo 1: Iterando sobre uma Lista

frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)
#Fruta é a variavel de iteração, poderia ser qualquer nome.

# O que acontece:

# Na 1º repetição, fruta será "maçã".
# Na 2º repetição, fruta será "banana".
# Na 3º repetição, fruta será "cereja".
# O FIM do loop é depois de processar todos os itens da lista.

# Exemplo 2: Usando range() para Iterar um Número Específico de Vezes
# A função range() é muito útil com for loops para gerar sequências de números.

# range(stop)
# range(start, stop)
# range(start, stop, step)

# range(stop): Gera números de 0 até stop-1.
for i in range(5): # Gera 0, 1, 2, 3, 4
    print(i)

# range(start, stop): Gera números de start até stop-1.
for i in range(1, 6): # Gera 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step): Gera números de start até stop-1, pulando de step em step.
for i in range(0, 10, 2): # Gera 0, 2, 4, 6, 8
    print(i)

# Como o for loop se encaixa no exercício do fatorial (que pulamos):

# Para calcular o fatorial de um número n, você multiplicaria todos os números de 1 a n. Um for loop seria a ferramenta perfeita para isso, iterando de 1 até n e acumulando o produto.

# Exemplo 1: Iterando sobre uma string
empresa = "INFINITY SCHOOL"
for letra in empresa:
    print(letra)
'''
I
N
F
I
N
I
T
Y

S
C
H
O
O
L
'''

# Exemplo 2: Usando a função range() para repetir um número de vezes
for i in range(5): # Vai de 0 a 4 (5 vezes)
    print("Contagem:", i)
'''
Contagem: 0
Contagem: 1
Contagem: 2
Contagem: 3
Contagem: 4

No primeiro exemplo, cada letra da string "INFINITY SCHOOL" é impressa em uma nova linha. No segundo, a frase "Contagem: " é impressa junto com o número atual da iteração (0 a 4).'''

'''Exemplo usando while:
O while é usado para executar um bloco de código enquanto uma condição for verdadeira. '''

x = int(input("Digite um número positivo e inteiro: "))
while x <= 0:
    print(f"{x} é negativo, digite um numero positivo")
    x = int(input("Digite um número positivo e inteiro: "))

print(f"Parabéns o número digitado foi: {x}")

print("---- FIM ----")


'''Neste caso, o bloco de código dentro do while será executado enquanto contador for menor que 3. A cada repetição, o contador é aumentado em 1. Quando contador chega a 3, a condição contador < 3 se torna falsa e o loop termina. 
Repetição número: 0
Repetição número: 1
Repetição número: 2
Fim do loop.'''

'''
Instruções break e continue:

break: Força a interrupção do laço sempre que encontrada no bloco de código, geralmente após uma instrução condicional if.

continue: Interrompe a execução do ciclo sem interromper a execução do laço de repetição. A iteração atual do loop será interrompida, mas o programa retornará ao topo do loop. Geralmente fica dentro do bloco de código abaixo da instrução de loop, após um if condicional.

6. Variável Flag:

Uma variável definida apenas para definir um valor, geralmente através de atribuições usando operadores como +=, -= ou *=.

---------------- Seção 2. Operadores de Comparação ---------------- 
São operadores que analisam os valores de uma expressão e retornam um valor booleano (verdadeiro ou falso).

Exemplos incluem:
== (igual a) 
!= (diferente de) 
> (maior que) 
< (menor que) 
>= (maior ou igual a) 
<= (menor ou igual a) 

3. Estruturas Condicionais (if, else, elif):
Instrução if: Analisa uma condição e, com base no resultado, executa uma determinada ação. A ação é executada somente se a condição testada for verdadeira.

Instrução else: Se a condição do if não for verdadeira, a opção else é executada.

Estrutura Condicional Aninhada (if, elif, else): Utilizada quando são necessários mais de dois resultados (condições), como em um semáforo. 

elif é a junção de else + if.

Estrutura Condicional Simples & Aninhada

Foca em como um programa pode tomar decisões com base em condições. É aqui que usamos os "Operadores de comparação" (como >, <, ==, >=, <=, !=) e "Operadores Lógicos" (como and, or, not) que vimos anteriormente para controlar o fluxo do programa.

Basicamente, as estruturas condicionais permitem que seu código execute diferentes blocos de instruções dependendo se uma condição é verdadeira (True) ou falsa (False).

Existem algumas formas principais de fazer isso:
'''
'''
1. Estrutura Condicional Simples (if)
Propósito: Executa um bloco de código somente se uma condição específica for verdadeira. Se a condição for falsa, esse bloco de código é simplesmente ignorado.

Palavra-chave: if

Exemplo:
'''
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
#(Se a idade for 15, a mensagem não aparecerá.)


'''
2. Estrutura Condicional Composta (if-else)
Propósito: Permite que o programa execute um bloco de código se a condição for verdadeira e um bloco diferente se a condição for falsa. É uma escolha entre duas alternativas.

Palavras-chave: if, else

Exemplo:
'''
temperatura = 28
if temperatura > 25:
    print("Está quente!")
else:
    print("Não está quente.")
#(Se a temperatura fosse 20, a mensagem "Não está quente." apareceria.)
'''
3. Estrutura Condicional Encadeada (if-elif-else)
Propósito: Usada para verificar múltiplas condições em sequência. O programa verifica a primeira condição (if). Se for falsa, ele passa para a próxima condição (elif). Isso continua até que uma condição verdadeira seja encontrada ou, se nenhuma for verdadeira, o bloco else final é executado como um "curinga".

Palavras-chave: if, elif (abreviação de "else if"), else

Exemplo:
'''

nota = 85
if nota >= 90:
    print("Conceito A")
elif nota >= 80: # Se a nota não for >= 90, mas for >= 80
    print("Conceito B")
elif nota >= 70: # Se a nota não for >= 80, mas for >= 70
    print("Conceito C")
else: # Se nenhuma das anteriores for verdadeira
    print("Conceito D")
# (No exemplo, "Conceito B" seria impresso.)

'''
4. Estruturas Condicionais Aninhadas (Nested ifs)
Propósito: Uma estrutura condicional dentro de outra estrutura condicional. Isso é útil quando a decisão de um nível depende de uma decisão anterior.

Exemplo:
'''

idade = 20
tem_cnh = True

if idade >= 18:
    print("Você é maior de idade.")
    if tem_cnh: # Este 'if' está aninhado dentro do primeiro 'if'
        print("Você pode dirigir.")
    else:
        print("Você precisa tirar sua CNH para dirigir.")
else:
    print("Você é menor de idade e não pode dirigir.")
# (No exemplo, "Você é maior de idade." e "Você pode dirigir." seriam impressos.)

'''
Nós usamos essas estruturas em vários exercícios anteriores, como:
=> Identificar o maior/menor número.
=> Dizer "Bom Dia!"/"Boa Tarde!"/"Boa Noite!".
=> Calcular raízes de equações de segundo grau (com as diferentes condições para Delta e a).
=> Verificar vogal/consoante.

Essas estruturas são o coração da lógica de decisão em qualquer programa!

4. Operadores Lógicos:

Indicam ao sistema a maneira como uma premissa deve se relacionar com outra dentro de uma estrutura condicional para retornar verdadeiro ou falso.

São usados para controle de fluxo de execução e tomadas de decisão.

Exemplos incluem:

and: Verdadeiro somente se ambos os operadores forem verdadeiros.
or: O resultado será verdadeiro bastando apenas uma das comparações ser verdadeira.
not: Utilizado para inverter o resultado de uma determinada condição.


5. Estruturas de Repetição (Laços):

Laço for: Recurso para desenvolver tarefas repetitivas em um loop contínuo. O loop funciona até uma condição ser satisfeita.

O loop realiza iterações, ou seja, uma repetição que analisa, percorre ou repete finita ou infinitamente uma estrutura, coleção ou sequência de valores.

A função range() permite especificar o início da sequência, o valor final e o passo. O único parâmetro obrigatório é o que define o último elemento da sequência.

Laço while: Utilizado quando um determinado bloco de código deve ser executado enquanto uma condição específica for atendida. Sai da estrutura de repetição quando a condição não for mais satisfeita.

Laço while infinito: Considerado infinito quando sua condição estabelecida nunca retorna False. Usado quando não se sabe quantas vezes o programa irá rodar ou executar um comando, geralmente com uma condição para o usuário escolher quando parar.


---------------- Seção 04: Laço de Repetição While ---------------- 
O laço while é outro tipo de estrutura de repetição fundamental em Python, mas ele funciona de uma maneira um pouco diferente do for.

For Loop: É geralmente usado quando você sabe quantas vezes quer repetir um bloco de código (por exemplo, "para cada item nesta lista", "para cada número de 1 a 10").

While Loop: É usado quando você quer repetir um bloco de código enquanto uma determinada condição for verdadeira. A repetição continua indefinidamente até que a condição se torne falsa.

Como funciona o while loop:
Condição: O while loop começa com a palavra-chave while, seguida de uma condição.

Verificação: Antes de cada repetição (ou "iteração"), o loop verifica se essa condição é True (verdadeira).

Execução:

=> Se a condição for True, o código dentro do bloco while (o corpo do loop) é executado.
=> Se a condição for False, o loop para, e o programa continua executando o código que vem depois do while loop.

Atualização da Condição: É crucial que, em algum lugar dentro do corpo do while loop, haja algo que faça com que a condição se torne False em algum momento. Caso contrário, você terá um loop infinito (o programa nunca para de rodar, pois a condição nunca se torna falsa).

Sintaxe Básica:
'''
# 1. Inicialize qualquer variável que sua condição 'while' vai usar
contador = 0

# 2. Defina a condição que, enquanto for True, o loop vai rodar
while contador < 5:
    # 3. Código a ser repetido (corpo do loop)
    print(f"O contador é: {contador}")

    # 4. ATUALIZE a variável que afeta a condição para evitar um loop infinito
    contador += 1 # Isso fará o contador aumentar até 5, tornando a condição falsa
'''
Exemplo prático: Contagem regressiva (com while em vez de for)

# 1. Inicializa o número de onde vamos começar a contagem
numero = 5

# 2. A condição é: enquanto o número for maior ou igual a 0
while numero >= 0:
    print(numero) # Imprime o número atual
    numero -= 1   # Decrementa o número para que a condição eventualmente se torne falsa (Evita loop infinito!)

print("FIM!") # Mensagem final após o loop

Nesse exemplo, o loop continua enquanto numero for 5, 4, 3, 2, 1, 0. Quando numero se torna -1, a condição numero >= 0 se torna False, e o loop para.

Entendeu como o while loop difere do for e quando ele é mais útil? Ele é perfeito para situações onde você não sabe exatamente quantas repetições serão necessárias, mas sim enquanto uma condição específica for mantida.




'''
