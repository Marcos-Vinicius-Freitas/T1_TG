"""
Discentes: Higor Vinícius Magalhães Correia e Marcos Vinicius
"""

import csv
import heapq

def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo:
        municipios = csv.reader(arquivo)
        linhas = []
        for linha in municipios:
            if linha and any(celula.strip() for celula in linha):
                linhas.append(linha)      

    cabecalho = linhas[0]
    nomes_municipios = []
    for celula in cabecalho[1:]:
        nomes_municipios.append(celula.strip())

    matriz_string = []
    for linha in linhas[1:]:
        nova_linha = []
        for celula in linha[1:]:
            nova_linha.append(celula.strip())
        matriz_string.append(nova_linha)

    return nomes_municipios, matriz_string

def tratar_matriz(matriz_string):
    soma = 0
    for linha in matriz_string:
        for celula in linha:
            if celula.strip().lower() != "inf":
                soma += int(celula)
    
    soma = soma + 1

    matriz_convertida = []
    for linha in matriz_string:
        nova_linha = []
        for celula in linha:
            celula_limpa = celula.strip().lower()
            if celula_limpa == "inf":
                nova_linha.append(soma)
            else:
                nova_linha.append(int(celula))
        matriz_convertida.append(nova_linha)

    return matriz_convertida, soma

def escolher_cidade(nomes, mensagem):
    print(mensagem)
    for i, nome in enumerate(nomes):
        print(f"  [{i}] {nome}")

    while True:
        escolha = input("Digite o numero ou o nome da cidade: ").strip()

        if escolha.isdigit() and 0 <= int(escolha) < len(nomes):
            return int(escolha)

        for i, nome in enumerate(nomes):
            if nome.lower() == escolha.lower():
                return i

        print("Entrada invalida, tente novamente.")

def dijkstra(matriz, origem, destino):
    n = len(matriz)
    distancia = [float("inf")] * n
    conhecidos = set()
    anterior = {origem: None}

    distancia[origem] = 0
    fila = [(0, origem)]

    while fila:
        distancia_atual, u = heapq.heappop(fila)

        if u in conhecidos:
            continue
        else:
            conhecidos.add(u)

        if u == destino:
            break
        else:
            for v in range(n):
                peso = matriz[u][v]

                if v != u and distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
                    anterior[v] = u
                    heapq.heappush(fila, (distancia[v], v))

    if distancia[destino] == float("inf"):
        return None, []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]
    caminho.reverse()
    return distancia[destino], caminho

def main():
    nomes, matriz_string = ler_csv("./municipios.csv")

    matriz, valor_inf = tratar_matriz(matriz_string)

    origem = escolher_cidade(nomes, "\nCidades disponiveis (origem):")
    destino = escolher_cidade(nomes, "\nCidades disponiveis (destino):")

    distancia, caminho = dijkstra(matriz, origem, destino)

    if distancia is None:
        print("Nao existe caminho entre a origem e o destino.")
    
    caminho_nomes = [nomes[i] for i in caminho]
    print(f"Distancia total: {distancia}")
    print("Percurso: " + " -> ".join(caminho_nomes))


if __name__ == "__main__":
    main()
