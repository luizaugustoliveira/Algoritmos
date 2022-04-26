def contagem(lista, elemento):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1
    
    return contador


def meu_remove(lista, elemento):
    for i in range(len(lista) -1, -1 , -1):
        if lista[i] == elemento:
            lista.pop(i)


lista = [10, 20, 30, 40, 20, 50, 60, 40]

i = 0
while i < len(lista):
    if contagem(lista, lista[i]) > 1:
        meu_remove(lista, lista[i])
    i += 1

print(lista)
 