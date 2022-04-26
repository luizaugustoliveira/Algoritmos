# luiz.augusto.farias@ccc.ufcg.edu.br

def agrupa_negativos(lista):
    negativos = []
    nao_negativos = []
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos.append(lista[i])
        
        if lista[i] > 0:
            nao_negativos.append(lista[i])

    numeros = {}

    numeros["nao-negativos"] = nao_negativos
    numeros["negativos"] = negativos
    
    return numeros


assert agrupa_negativos([10, -2, -7, 8]) == {"nao-negativos":[10, 8], "negativos":[-2,-7]}
assert agrupa_negativos([-1, -5]) == {"nao-negativos":[ ], "negativos":[-1, -5]}
assert agrupa_negativos([0, -111, 0, 1814651]) == {"nao-negativos":[1814651], "negativos":[-111]}