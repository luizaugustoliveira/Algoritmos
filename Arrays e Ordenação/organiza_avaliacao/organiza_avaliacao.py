def organiza_avaliacao(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i][1] == -1:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice += 1

    for i in range(indice, len(lista)):
        if lista[i][1] == 0:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice += 1      

    for i in range(indice, len(lista)):
        if lista[i][1] == 1:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice += 1 


l = [("Pedro", 1), ("Tito", -1), ("Zeca", 1), ("Lucca", -1),("Mirna", 0)]
assert organiza_avaliacao(l) == None
assert l == [("Tito", -1), ("Lucca", -1), ("Mirna", 0), ("Pedro", 1), ("Zeca", 1)]
