#luiz.augusto.farias@ccc.ufcg.edu.br

def negativos_no_fim(lista):
    indice = -1
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] < 0:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice += -1


fila = [12, -21, -35, 8, 12, 15]
assert negativos_no_fim(fila) == None
assert fila == [12, 12, 15, 8, -21, -35]