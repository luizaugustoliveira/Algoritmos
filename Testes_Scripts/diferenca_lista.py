def meu_in(sequencia, elemento):
    for valor in sequencia:
        if valor == elemento:          
            return True
    return False

def diferenca_listas(lista1, lista2):
    for i in range(len(lista1) - 1, -1, -1):
        if meu_in(lista2, lista1[i]):
            lista1.pop(i) 

    return lista1

lista1 = [2, 1, 3, 4]
lista2 = [2]
diferenca_listas(lista1, lista2) == [1, 3, 4]
assert lista1 == [1, 3, 4]
lista1 = [1, 3, 4]
lista2 = [4]
diferenca_listas(lista1, lista2) == [1, 3]
assert lista1 == [1, 3]