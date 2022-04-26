lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]

def encontra_menores(num, lista):
    for elemento in lista:
        if elemento < num:
            menor = elemento
            break
        else:
            menor = -1
        
    return menor

assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4

