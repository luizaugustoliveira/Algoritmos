# luiz.augusto.farias@ccc.ufcg.edu.br

def normaliza_matriz(M):
    soma = 0
    contador = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            soma += M[i][j]
            contador += 1

    media = int(soma / contador)

    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] -= media

    return M
