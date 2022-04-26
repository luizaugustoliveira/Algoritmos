def insere_ordenanda(lista, num):
    lista.append(num)
    lista.pop(0)
    lista.pop(0)
    
    for i in range(len(lista) - 1, -1, -1):
        if num > lista[i]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
    return lista

print(insere_ordenanda([9, 7, 5, 4, 3, 1], 2))