def ultimo(lista_):
    return lista_[-1]

def bubblesort(lista):
    for k in range(len(lista) - 1, 0, -1):
        for i in range(k):
            if ultimo(lista[i]) > ultimo(lista[i + 1]):
                elemento = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = elemento


lista = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]
bubblesort(lista)
print(lista)