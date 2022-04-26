def multiplica(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

lista1 = [3, 1, 2, 3]
print(multiplica(lista1))