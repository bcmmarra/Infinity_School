'''
and – Retorna True se todas as condições forem verdadeiras.

TABELA VERDADE
A	    B	    A and B
True	True	True
True	False	False
False	True	False
False	False	False
'''
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")


'''
#or – Retorna True se pelo menos uma condição for verdadeira.    

A   	B   	A or B
True	True	True
True	False	True
False	True	True
False	False	False
'''
dia = "sábado"
feriado = False

if dia == "sábado" or dia == "domingo" or feriado:
    print("Hoje não tem aula.")

'''
#not – Inverte o valor de uma condição.

A	    not A
True	False
False	True
'''
chovendo = False

if not chovendo:
    print("Pode sair para passear!")
    
    
'''Utilizando Multiplos Operadores Lógicos'''

idade = 20
tem_carteira = False
tem_carteira_provisoria = True

if idade >= 18 and (tem_carteira or tem_carteira_provisoria ):
    print("Pode dirigir.")