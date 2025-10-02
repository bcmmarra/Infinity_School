'''3. Construa um programa para calcular a área de convivência
de uma escola cujo formato é circular. Para isso, o usuário deve
informar o valor do raio.'''

from math import pi                             #Chamada da bibliotéca math e importação da constante pi.
raio = float(input("Digite o raio da área: "))
area = pi * (raio ** 2)
print(f"Área = {area:.2f}m")


'''Comentários sobre a resolução
Relembrando do conteúdo estudado em Geometria, a área limitada
por uma circunferência corresponde ao produto entre a
constante e o raio da circunferência, a fórmula que usamos é a seguinte:
A=
pi
timesr²
 
Onde:

A é a área
pi (Pi) é uma constante matemática (aproximadamente 3.14159)
"times": No contexto informal, significa "vezes" ou "multiplicado por".
"r": Geralmente representa o raio de um círculo ou esfera em fórmulas matemáticas e científicas.
"²" (o pequeno 2 sobrescrito): Indica que o número ou variável imediatamente antes dele deve ser elevado ao quadrado, ou seja, multiplicado por ele mesmo (r * r).

Sintaxe
area = pi * (raio ** 2)


'''