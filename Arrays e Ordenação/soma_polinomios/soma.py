# luiz.augusto.farias@ccc.ufcg.edu.br

def soma_polinomios(p1, p2):
    valores = []
    if len(p1) != len(p2):
        if len(p1) < len(p2):
            nova_lista = []
            for i in range(len(p2) - len(p1)):
                nova_lista.append(p2[i])
            indice = -1
            while True:
                valores.append(p1[indice] + p2[indice])
                indice += -1
                if abs(indice) -1 == len(p1): break

        if len(p1) > len(p2):
            nova_lista = []
            for i in range(len(p1) - len(p2)):
                nova_lista.append(p1[i])
            indice = -1
            while True:
                valores.append(p1[indice] + p2[indice])
                indice += -1
                if abs(indice) -1 == len(p2): break

        lista = []
        for i in range(len(valores) -1, -1, -1):
            lista.append(valores[i])

        retorno = nova_lista + lista
    else:
        indice = -1
        while True:
            valores.append(p1[indice] + p2[indice])
            indice += -1
            if abs(indice) -1 == len(p2): break

        lista = []
        for i in range(len(valores) -1, -1, -1):
            lista.append(valores[i])

        retorno = lista

    return retorno


p1 = [3, 4, -5]
p2 = [5, 0, 0, 0, 2, 0, -1]
assert soma_polinomios(p1, p2) == [5, 0, 0, 0, 5, 4, -6]
