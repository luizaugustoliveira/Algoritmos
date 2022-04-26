def remove_pares(lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] % 2 == 0:
            lista.pop(i)
    return lista

print(remove_pares([7,8, 120, 25, 44, 20, 27]))