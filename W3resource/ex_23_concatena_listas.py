lista = [[2,4,3],[1,5,6], [9], [7,9,0]]

nova_lista = []
for i in range(len(lista)):
    for j in range(len(lista[i])):
        nova_lista.append(lista[i][j])

print(nova_lista)