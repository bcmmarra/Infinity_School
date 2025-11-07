
# ## Atividade 1

# Implemente uma classe `Livro`.

# A classe `Livro` deve representar uma obra literária, contendo os seguintes atributos:

# - titulo (str): Título do livro.
# - editora (str): Nome da editora.
# - ano (int, opcional): Ano de publicação. Caso não seja informado, deve assumir `None`.
# - autor (str, opcional): Nome do autor. Também pode ser `None`.

# Exemplo de uso:
# l1 = Livro("Hábitos Atômicos", "Alta Life", 2019, "James Clear")
# print(l1.titulo)  # "Hábitos Atômicos"

# l2 = Livro("Biblía", "Deus")
# print(l1.titulo)  # "Biblía"
# print(l1.ano)  # None

class Livro: 
    def __init__(self, titulo: str, editora: str, ano: int = None, autor: str = None) -> None:
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.autor = autor

l1 = Livro("Hábitos Atômicos", "Alta Life", 2019, "James Clear")
print(f'Título: {l1.titulo}')
print(f'Editora: {l1.editora}')
print(f'Ano: {l1.ano}')
print(f'Autor: {l1.autor}')

print('=-'*20)

l2 = Livro("Biblía", "Deus")
print(f'Título: {l2.titulo}')
print(f'Editora: {l2.editora}')
print(f'Ano: {l2.ano}')
print(f'Autor: {l2.autor}')

print('=-'*20)

# Passando de forma nomeada
l3 = Livro(
    titulo="Cabeça Fria Coração Quente",
    editora="Cultura",
    ano=2022,
    autor='Abel Ferreira')

print(f'Título: {l3.titulo}')
print(f'Editora: {l3.editora}')
print(f'Ano: {l3.ano}')
print(f'Autor: {l3.autor}')

print('=-'*20)
