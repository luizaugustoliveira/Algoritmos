# luiz.augusto.farias@ccc.ufcg.edu.br   

def busca_matriz(m, e):
    linhas = len(m)
    colunas = len(m[0])

    existe = False
    indices = []
    for i in range(linhas):
        for j in range(colunas):
            if m[i][j] == e:
                existe = True
                posicao_linha = i    
                posicao_coluna = j

                indices.append((posicao_linha, posicao_coluna))


    if existe == False:
        return []
    else:
        return indices

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
