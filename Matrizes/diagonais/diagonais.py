# luiz.augusto.farias@ccc.ufcg.edu.br     

def diagonais(M):
    matriz = [[],[]]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j:
                matriz[0].append(M[i][j])

            if i + j == len(M) - 1:
                matriz[1].append(M[i][j])

    return matriz


M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

assert diagonais(M) == [[1,5,9],[3,5,7]]