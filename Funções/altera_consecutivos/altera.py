def inverte2a2(lista):
    if len(lista) % 2 == 0:
        for i in range(len(lista)):
            if i != len(lista):
                if i % 2 == 0:
                    lista[i], lista[i + 1] = lista[i +1], lista[i]

    if len(lista) % 2 == 1:
        for i in range(len(lista) -1):
            if i != len(lista) -1:
                if i % 2 == 0:
                    lista[i], lista[i + 1] = lista[i +1], lista[i]        


seq = [1,2,3,4,5,6]
inverte2a2(seq)
assert seq == [2,1,4,3,6,5]

seq = [1,2,3,4,5]
inverte2a2(seq)
assert seq == [2,1,4,3,5]