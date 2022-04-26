def gera_filas(fila, n):
    lista = []
    for i in range(n):
        lista.append([])

    for i in range(len(fila)):
        indice = i % n
        lista[indice].append(fila[i])
    return lista