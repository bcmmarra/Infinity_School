# Uma função pode devolver um valor com a palavra return.

def soma(a,b):
    return a + b

# Chamando a função
resultado = soma(3, 5)  # O valor retornado pela função volta para o local de chamada.
print(resultado)        # saída: 8

# - Declaramos a função `soma` que precisa de 2 parâmetros: `a` e `b`
# - A função `soma` retorna a soma dos parâmetros utilizando o `return`
# - A função `soma` é executada, o valor de retorno volta para o local de chamada da função e é armazenado em `resultado`

# OBS: Mesmo que a gente não utilize o return explicitamente, toda função retorna alguma coisa, por padrão é o None 

### Entrada, Processamento e Saída
# Podemos comparar uma função com a estrutura básica de qualquer programa:

# Etapa           |      Componente      | Exemplo na Função soma(a, b)
# Entrada         |      Parâmetros      | valores a e b
# Processamento   |      Processamento   | cálculo de a + b
# Saída           |      Retorno         | resultado devolvido (return)

