# luiz.augusto.farias@ccc.ufcg.edu.br
# Remove Ocorrências

def remove_ocorrencias(lista, elemento):
    for i in range(len(lista) -1, -1, -1):
        if lista[i] == elemento:
            retorno = lista[i]
            lista.pop(i)
        else:
            retorno = None
    
    return retorno
    
    
lista = [1, "Prog1", 3.4, 1]
assert remove_ocorrencias(lista, 1) == 1
assert lista == ["Prog1", 3.4]
lista = [1, "Prog1", 3.4, 1]
assert remove_ocorrencias(lista, 2) == None
assert lista == [1, "Prog1", 3.4, 1]