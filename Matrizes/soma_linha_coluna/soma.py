# luiz.augusto.farias@ccc.ufcg.edu.br

def soma_linha_e_coluna(matriz,l,c):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                if i == l:
                    soma += matriz[i][j]

                if j == c:
                    soma += matriz[i][j]

    return soma


matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]
assert soma_linha_e_coluna(matriz,1,1) == 20
assert soma_linha_e_coluna(matriz,0,0) == 18