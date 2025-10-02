''' 2. Construa um programa que receba do usuário a variação do 
deslocamento de um objeto (em metros) e a variação do tempo 
percorrido (em segundo). Ao fim, o programa deve calcular a 
velocidade média, em m/s, do objeto.'''

deslocamento = float(input("Digite o deslocamento (em metros): "))
tempo = float(input("Digite o tempo (em segundos): "))
velocidade = deslocamento / tempo
print(f"A velocidade em m/s é de {velocidade:.2f} metro(s) por segundo.")


'''
Comentários sobre a resolução
Recordando das aulas de Cinemática, sabemos que
O enunciado da questão diz que o usuário informará a variação
do deslocamento (isto é, Δt) e a variação do tempo (ou seja, Δt).
Então, para calcular o que foi pedido, basta dividir o primeiro
valor informado pelo usuário pelo segundo valor. No entanto, é
importante relembrar que a) input() é usada para receber os
dados de entrada e b) ela sempre retorna uma string. Portanto,
é preciso fazer as conversões dos valores de entrada para
float, porque, por exemplo, o deslocamento pode ser 10,23
metros (valor real) e/ou o tempo percorrido 2,10 segundos (valor real).
Lembre-se que, em um valor real, por conta do separador decimal
americano, quem separa a parte inteira da decimal é o
ponto e não a vírgula. Portanto 3,14 deve ser substituído por
3.14.
'''