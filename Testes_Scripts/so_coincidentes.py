def so_coincidentes(M1, M2):
    nova_matriz = []
    for i in range(len(M1)):
        nova_matriz.append([])

    linhasm1 = len(M1)
    colunasm1 = len(M1[0])

    for i in range(linhasm1):
        for j in range(colunasm1):
            if M1[i][j] != M2[i][j]:
                nova_matriz[i].append(0)
            else:
                nova_matriz[i].append(M1[i][j])
    
    return nova_matriz

M1 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
M2= [[10, 11, 12],
[13, 14, 15],
[ 7, 8, 9]]
M3= [[ 1, 2, 3],
[13, 14, 15],
[16, 17, 18]]
assert so_coincidentes(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]
assert so_coincidentes(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]