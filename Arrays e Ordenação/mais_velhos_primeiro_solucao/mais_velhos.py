def idosos_inicio(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] >= 60:
            lista[i], lista[indice] = lista[indice], lista[i]
            indice += 1


fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
print(idosos_inicio(fila))
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]