# luiz.augusto.farias@ccc.ufcg.edu.br
def bubblesort(lista):
    passagens = len(lista) - 1
    for j in range(len(lista)):
        for i in range(passagens):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        
    return lista


