# luiz.augusto.farias@ccc.ufcg.edu.br

def zera_acima_ou_abaixo(m):
    soma_acima = 0
    soma_abaixo = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j > i:
                soma_acima += m[i][j]
         
            if i > j:
                soma_abaixo += m[i][j]

    for i in range(len(m)):
        for j in range(len(m[0])):
            if soma_acima > soma_abaixo:
                if j > i:
                    m[i][j] = 0
            
            if soma_abaixo > soma_acima:
                if i > j:
                    m[i][j] = 0

    return m

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
zera_acima_ou_abaixo(M)
assert M == [[1,2,3],
             [0,5,6],
             [0,0,9]]