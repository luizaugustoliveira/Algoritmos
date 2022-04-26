# luiz.augusto.farias@ccc.ufcg.edu.br
# Subsequencia 1, 2, 3

def meu_in(sequencia, elemento):
    for valor in sequencia:
        if valor == elemento:          
            return True
    return False


def encontra(lista):
    ordem_indices = []
    for i in range(len(lista)):
        if meu_in(lista, 1) == True and meu_in(lista, 2) == True and meu_in(lista, 3) == True:
            if lista[i] == 1:
                ordem_indices.append(i)
                break
    
    indice_2 = 0
    for i in range(len(lista)):
        if meu_in(lista, 1) == True and meu_in(lista, 2) == True and meu_in(lista, 3) == True:
            if lista[i] == 2:
                if i > indice_2:
                    indice_2 = i
    ordem_indices.append(indice_2)
    
    indice_3 = 0
    for i in range(len(lista)):
        if meu_in(lista, 1) == True and meu_in(lista, 2) == True and meu_in(lista, 3) == True:
            if lista[i] == 3:
                if i > indice_3:
                    indice_3 = i
    ordem_indices.append(indice_3)

    return ordem_indices


def tem123plus(l):
    for i in range(len(l)):
        if meu_in(l, 1) == True and meu_in(l, 2) == True and meu_in(l, 3) == True:
            lista = encontra(l)
            if lista[0] < lista[1] and lista[0] < lista[2]:
                return lista[0]

    else:
        return -1


assert tem123plus([3, 2, 1, 2, 3]) == 2
assert tem123plus([4, 1, 1, 1, 4, 2, 3]) == 1
assert tem123plus([1, 2, 2, 3]) == 0
assert tem123plus([1, 2, 2, 4]) == -1
assert tem123plus([]) == -1




    
    




