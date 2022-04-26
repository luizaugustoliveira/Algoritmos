def meu_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


def remove_duplicates(lista):
    nova_lista = []
    for i in range(len(lista)):
        if meu_in(nova_lista ,lista[i]) == False:
            nova_lista.append(lista[i])
    return nova_lista

print(remove_duplicates([10,20,30,20,10,50,60,40,80,50,40]))