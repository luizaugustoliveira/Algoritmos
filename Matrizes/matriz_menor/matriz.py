# luiz.augusto.farias@ccc.ufcg.edu.br    

def matriz_menor(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])

    matriz = []
    for i in range(linhas):
        matriz.append([])

    for i in range(linhas):
        for j in range(colunas):
            if matriz1[i][j] < matriz2[i][j]:
                matriz[i].append(matriz1[i][j])
            else:
                matriz[i].append(matriz2[i][j])

    return matriz

M1= [[1,2,3],
    [13,14,15],
    [7,8,9]]

M2= [[10,11,12],
    [4,5,6],
    [7,8,9]]

M3= [[1,2,3],
    [0,0,0],
    [7,8,9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]
