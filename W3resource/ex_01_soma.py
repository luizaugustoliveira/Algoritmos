def soma(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

lista1 = [10, 12, 20, 22]
print(soma(lista1))