# Faça um programa para realizar uma votação que será armazenada em um dicionário, onde os candidatos são as chaves, e o valor é a quantidade de votos. O programa iniciará com os candidatos preenchidos e deverá perguntar quantos votos serão realizados. Ao final mostre o resultado da votação.

# Seu código inicial está ótimo
candidatos = {
    'CandidatoA': 0,
    'CandidatoB': 0,
    'CandidatoC': 0
}


eleitores = int(input('Informe a quantidade de eleitores: '))

# Lista com os nomes dos candidatos para facilitar a escolha por número
lista_nomes = list(candidatos.keys())

print('\n***** Lista de Candidatos *****')
for i, nome in enumerate(lista_nomes):
    print(f'- [{i + 1}] {nome}')

# Votação
for i in range(eleitores):
    print(f'\nEleitor {i + 1} de {eleitores}')
    
    voto = int(input('Número do Candidato: '))
        
    # Verifica se o voto é um número válido na lista de candidatos
    if 1 <= voto <= len(lista_nomes):
        # Obtém o nome do candidato usando o índice (voto - 1)
        candidato_escolhido = lista_nomes[voto - 1]
        
        # Incrementa o voto no dicionário
        candidatos[candidato_escolhido] += 1
        print('Voto registrado!')
    else:
        print('Voto inválido. Por favor, escolha um número da lista.')
    
# Exibe o resultado final
print('\n--- Resultado da Votação ---')
for nome, votos in candidatos.items():
    print(f'{nome}: {votos} votos')

