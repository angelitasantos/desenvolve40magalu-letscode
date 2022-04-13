matriz = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

tamanho_rios = []
coordenada_rios = []
rios = []

def contar_rios(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (matriz[linha][coluna] == 1):
                matriz[linha][coluna] = -1
                tamanho_rios.append(calcular_tamanho(matriz, linha, coluna))
                coordenada_rios.append([linha,coluna])
    return tamanho_rios


def mostrar_rio(self):
    print()
    for coordenada, tamanho in zip(coordenada_rios, tamanho_rios):
        rios.append([coordenada,tamanho])
        print(f'O rio que começa na {coordenada[0]+1}ª linha com a {coordenada[1]+1}ª coluna tem tamanho: {tamanho}')
    print()


def calcular_tamanho(matriz, linha, coluna):
    tamanho = 1
    if linha + 1 < len(matriz) and matriz[linha + 1][coluna] == 1:
        matriz[linha + 1][coluna] = -1
        tamanho += calcular_tamanho(matriz, linha + 1, coluna)

    if linha - 1 >= 0 and matriz[linha - 1][coluna] == 1:
        matriz[linha - 1][coluna] = -1
        tamanho += calcular_tamanho(matriz, linha - 1, coluna)

    if coluna + 1 < len(matriz[linha]) and matriz[linha][coluna + 1] == 1:
        matriz[linha][coluna + 1] = -1
        tamanho += calcular_tamanho(matriz, linha, coluna + 1)

    if coluna - 1 >= 0 and matriz[linha][coluna - 1] == 1:
        matriz[linha][coluna - 1] = -1
        tamanho += calcular_tamanho(matriz, linha, coluna - 1)

    return tamanho



print(f'O tamanho dos rios são: {contar_rios(matriz)}')
mostrar_rio(matriz)
