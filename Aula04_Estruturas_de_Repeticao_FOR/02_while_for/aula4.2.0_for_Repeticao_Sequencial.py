'''- O `for` é uma estrutura de repetição **contada**.
Diferente do `while`, que depende de uma **condição lógica**, o `for` percorre **sequências de elementos** (listas, strings, ranges).
É muito útil quando sabemos **quantas vezes** queremos repetir algo ou quando precisamos **iterar sobre uma coleção de dados**.'''

#O que é range()?
#Uma função que gera uma sequência de números.
# range(início, fim, passo)

'''
**início** → valor inicial (padrão: 0)
**fim** → valor final (não incluso)
**passo** → incremento (padrão: 1)
'''

for i in range(0, 5, 1):
    print(i, end=' ')
    
print('Fim')


#Aqui estamos contando de 1 até 10 (11 -1) pulando de 2 em 2.
for i in range(1, 11, 2):
    print(i)


