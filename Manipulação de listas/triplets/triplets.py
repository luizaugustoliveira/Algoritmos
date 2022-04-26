def triplets(lista):
    listaNum = [0] * 10
    for x in range(len(lista)):
        listaNum[lista[x]] += 1

    for y in range(len(listaNum)):
        if listaNum[y] == 3:
            z = 0
    
            while z < len(lista):
                if lista[z] == y:
                    lista.pop(z)
                else:
                    z += 1


digitos = [1, 2, 1, 2, 1, 1]
assert triplets(digitos) == None
assert digitos == [1, 2, 1, 2, 1, 1]
        
digitos = [1, 1, 2, 2, 5, 1]
assert triplets(digitos) == None
assert digitos == [2, 2, 5]