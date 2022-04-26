def menor(lista):
    menor = lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor

print(menor([8, -3, 22, 12]))