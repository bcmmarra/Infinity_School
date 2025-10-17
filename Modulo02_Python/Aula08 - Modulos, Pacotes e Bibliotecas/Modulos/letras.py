# letras.py
def contar_total_vogais(texto: str) -> int:
    qtd_vogais = 0

    for letra in texto:
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            qtd_vogais += 1

    return qtd_vogais

def contar_vogais(texto: str) -> dict[str, int]:
    qtd_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for letra in texto:
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            qtd_vogais[letra.lower()] += 1

    return qtd_vogais