import csv

def ler_csv(caminho_arquivo):
    #Lê o arquivo CSV e o interpreta como uma lista de listas
    with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo:
        municipios = csv.reader(arquivo)
        #Cria uma lista das linhas de municipios.csv, ignorando linhas vazias
        linhas = [linha for linha in municipios if linha and any(c.strip() for c in linha)]

    cabecalho = linhas[0]
    #Ignora a primeira célula vazia
    nomes_municipios = [c.strip() for c in cabecalho[1:]]

    adjacencias_string = []
    #ignora a primeira linha (cabeçalho)
    for linha in linhas[1:]:
        adjacencias_string.append([celula.strip() for celula in linha[1:]])

    return nomes_municipios, adjacencias_string
