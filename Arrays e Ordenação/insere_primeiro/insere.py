# luiz.augusto.farias@ccc.ufcg.edu.br

def insere_ordenado_primeiro(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[indice] > lista[i]:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice +=1
        
    return lista


l1 = [5,2,6,9,11,13]
insere_ordenado_primeiro(l1)
assert l1 == [2,5,6,9,11,13]

l2 = [3,1,2,4]
insere_ordenado_primeiro(l2)
assert l2 == [1,2,3,4]