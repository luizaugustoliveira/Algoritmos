# luiz.augusto.farias@ccc.ufcg.edu.br

def soma_triangulo_superior(matriz):
    soma = 0
    if len(matriz) % 2 != 0:
        for i in range(len(matriz) // 2):
            for j in range(i + 1, len(matriz[0]) - (i + 1)):
                soma += matriz[i][j]

    if len(matriz) % 2 == 0:
        for i in range((len(matriz) // 2) - 1):
            for j in range(i + 1, len(matriz[0]) - (i + 1)):
                soma += matriz[i][j]

    return soma    
