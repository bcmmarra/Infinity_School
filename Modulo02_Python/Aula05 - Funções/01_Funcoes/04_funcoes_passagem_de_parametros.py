# Posicional
def mostrar_soma(a, b, c):
    print(a + b + c)
    
# Os valores são passados em ordem
# Dessa forma os argumentos são passados de forma respectiva para os parâmetros
mostrar_soma(1, 2, 3)

# Nomeada
def mostrar_soma(a, b, c):
    print(a + b + c)
    
# Os valores são passados diretamente para os parâmetros
# Dessa forma os argumentos são passados diretamente para os parâmetros, e podem ser passados em qualquer ordem
mostrar_soma(a=1, c=2, b=3)

# Posicional e Nomeada
def mostrar_soma(a, b, c):
    print(a + b + c)
    
# Os valores são passados em ordem e também diretamente.
# Dessa forma os primeiros parâmetros precisam ser posicionais e passados de forma respectiva, e os ultimos são passados diretamente em qualquer ordem.
mostrar_soma(1, c=2, b=3)