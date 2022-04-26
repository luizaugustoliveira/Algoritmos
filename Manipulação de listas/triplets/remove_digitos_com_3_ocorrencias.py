def contagem(lista, elemento):
    contador = 0
    for i in range(len(lista) -1, -1, -1):
        if lista[i] == elemento:
            contador += 1
    
    return contador


def meu_remove(lista, elemento):
    for i in range(len(lista) -1 , -1, -1):
        if lista[i] == elemento:
            lista.pop(i)


def triplets(lista):
    indice = 0
    while True:
        if indice > len(lista) - 1: break

        if contagem(lista, lista[indice]) == 3:
            meu_remove(lista, lista[indice])
        else:
            indice += 1


digitos = [1, 2, 1, 2, 1, 1]
assert triplets(digitos) == None
assert digitos == [1, 2, 1, 2, 1, 1]
        
digitos = [1, 1, 2, 2, 5, 1]
assert triplets(digitos) == None
assert digitos == [2, 2, 5]