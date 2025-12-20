produtos = []

def adicionar(nome: str, preco: float) -> None:
    """
    Adiciona um novo produto ao sistema.
    """
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar() -> None:
    """
    Exibe todos os produtos cadastrados.
    """
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"Nome: {p['nome']} | Preço: R$ {p['preco']:.2f}")

def filtrar_produtos(valor_limite: float = 100.0) -> list:
    """
    Retorna e exibe apenas os produtos com preço superior ao limite.
    """
    print(f"\n--- Produtos Caros (> R$ {valor_limite:.2f}) ---")
    caros = list(filter(lambda p: p['preco'] > valor_limite, produtos))
    
    if not caros:
        print("Nenhum produto encontrado nesta faixa de preço.")
    else:
        for p in caros:
            print(f"Nome: {p['nome']} | Preço: R$ {p['preco']:.2f}")
    return caros

# Exemplo de uso:
adicionar("Teclado Mecânico", 350.00)
adicionar("Mouse Gamer", 180.00)
adicionar("Mousepad", 45.00)
adicionar("Monitor 144Hz", 1200.00)
adicionar("Cabo HDMI", 30.00)

listar()
filtrar_produtos()