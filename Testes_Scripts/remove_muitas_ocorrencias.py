def conta(elemento, lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1
    return contador


def meu_in(sequencia, elemento):
    for valor in sequencia:
        if valor == elemento:          
            return True
    return False


def remove_muitas_ocorrencias(lista):
    remove = []
    for i in range(len(lista) -1, -1, -1):
        if conta(lista[i], lista) >= 3:
            remove.append(lista[i])

    for i in range(len(lista) -1, -1, -1):
        if meu_in(remove, lista[i]) == True:
            lista.pop(i)

        
digitos = [1, 1, 2, 2, 5, 1]
assert remove_muitas_ocorrencias(digitos) == None
assert digitos == [2, 2, 5]
digitos = [1, 2, 1, 2, 1, 1]
assert remove_muitas_ocorrencias(digitos) == None
assert digitos == [2, 2]