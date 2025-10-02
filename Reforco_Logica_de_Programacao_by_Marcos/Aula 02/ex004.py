# crie um lista onde verifica o valor do de cada item e classifica pela o valor se esta barato médio ou caro 

# 10 ate 30 barato 
# 40 a 60 médio 
# 70 pra cima caro 

# imprima uma mensagem relativa aos valores 

valores = [10,20,30,40,50,60,70,80,45,50,94,90,125]

for valor in valores:
    if valor > 0 and valor <= 39:
        print(f'O valor {valor:.2f} é Barato')
    elif valor > 40 and valor < 69:
        print(f'O valor {valor:.2f} é Médio')
    else:
        print(f'O valor {valor:.2f} é Caro')

