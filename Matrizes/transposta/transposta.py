def transposta(M):
    transposta = []

    for j in range(len(M[0])):
        transposta.append([])


    for j in range(len(M[0])):
        for i in range(len(M)):
            transposta[j].append(M[i][j])
            
    return transposta

M = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]

assert transposta(M) == [[1,2,3],
                         [1,2,3],
                         [1,2,3],
                         [1,2,3]]

assert M == [[1,1,1,1],
             [2,2,2,2],
             [3,3,3,3]]