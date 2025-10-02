# ## Atividade 4
# Crie dois conjuntos com os nomes de alunos de "Matemática" e "Programação".


Programacao = {'Bruno', 'Camila', 'Giovanna', 'Davi'} #Programacao
print(f'Turma de Programação = {Programacao}')

Matematica = {'Bruno', 'João Pedro', 'Lucia', 'Davi', 'Ana'} #Matematica
print(f'Turma de Matemática = {Matematica}')

# 1. Mostre quem está em **ambas as turmas**.
print(f'Ambas as Turmas = {Programacao.intersection(Matematica)}')
# Interseção → {'Davi', 'Bruno'}                => Retorna um novo conjunto contendo apenas os elementos que são iguais aos dois conjuntos

# 2. Mostre quem está **somente em Matemática**.
print(f'Somente Matemática = {Matematica.difference(Programacao)}')
# Diferença → {'João Pedro', 'Lucia', 'Ana'}    => Retorna um novo conjunto com os elementos que estão em A mas não estão em B ou vice-versa

# 3. Mostre todos os alunos sem repetição.
print(f'Todos os alunos = {Programacao.union(Matematica)}')
# União → {'Ana', 'Camila', 'João Pedro', 'Bruno', 'Davi', 'Giovana', 'Lucia'} => Combina todos os elementos dos dois conjuntos em um único conjunto sem repetir valores
