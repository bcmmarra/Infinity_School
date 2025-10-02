nomes = ['Bruno', 'Camila', 'Giovanna']
nomes.append('João Pedro')      # Adiciona no final da lista
nomes.insert(1, 'Davi')         # Insere na posição selecionada
nomes.pop()                     # Remove o ultimo da lista
nomes.remove('Camila')          # Remove o valor informado (se não existir da erro.)
print(nomes)

nomes.copy()               # Copia a lista
nomes2 = nomes.copy()               # Copia a lista
print(nomes2)
#nomes.clear()
