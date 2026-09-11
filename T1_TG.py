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

def tratar_matriz(matriz_string):
    # 1. Passo: Calcular a soma de todos os valores inteiros existentes
    soma = 0
    for linha in matriz_string:
        for celula in linha:
            # Se for numérico (com suporte a números com sinal/espaços), soma
            if celula.strip().lower() != "inf":
                soma += int(celula)
    
    # Substitui os "inf", por soma
    soma = soma + 1

    # 2. Passo: Criar a nova matriz convertida
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

# --- Exemplo de Execução ---

cidades, matriz_str = ler_csv("municipios.csv")

# Chama a nova função passando a matriz retornada pela ler_csv
matriz_str, valor_inf_usado = tratar_matriz(matriz_str)

print(f"Valor atribuído para 'inf' (Soma total + 1): {valor_inf_usado}\n")

print(cidades)

print(matriz_str)


#print("Matriz final de inteiros:")
#for linha in matriz_str:
#    print(linha)
