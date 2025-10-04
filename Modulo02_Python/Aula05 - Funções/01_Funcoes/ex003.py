# Crie uma função chamada apresentacao que recebe dois parâmetros: nome e sobrenome onde o sobrenome deve ser opcional (valor padrão deverá ser uma string vazia).

def apresentacao(nome, sobrenome=''):
    print(f'Meu nome é {nome} {sobrenome}, ...')

apresentacao('Gigi')
apresentacao('Bruno','Marra')



# Na primeira chamada, apresentacao('Gigi'), como não foi passado o sobrenome, ele assume o valor padrão '' (vazio). O resultado é: Meu nome é Gigi , ... — note o espaço extra antes da vírgula.
# Na segunda chamada, apresentacao('Bruno', 'Marra'), ambos os parâmetros são fornecidos, então a saída é: Meu nome é Bruno Marra, ....
# Para evitar o espaço extra quando o sobrenome não é fornecido, você pode ajustar a função assim:

def apresentacao(nome, sobrenome=''):
    if sobrenome:
        print(f'Meu nome é {nome} {sobrenome}, ...')
    else:
        print(f'Meu nome é {nome}, ...')

apresentacao('Gigi')
apresentacao('Bruno','Marra')


# ou com operador ternário

def apresentacao(nome, sobrenome=''):
    sobrenome = f' {sobrenome}' if sobrenome else ''
    print(f'Meu nome é {nome}{sobrenome}, ...')

apresentacao('Gigi')
apresentacao('Bruno','Marra')
