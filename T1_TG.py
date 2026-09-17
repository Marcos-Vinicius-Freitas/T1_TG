import csv

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


    main()
