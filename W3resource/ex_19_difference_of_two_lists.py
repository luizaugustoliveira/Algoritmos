def meu_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


def difference(lista1, lista2):
    nova_lista = []
    
    for x in lista1:
        if meu_in(lista2, x) == False:
            nova_lista.append(x)

    for y in lista2:
        if meu_in(lista1, y) == False:
            nova_lista.append(y)

    return nova_lista

print(difference([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]))