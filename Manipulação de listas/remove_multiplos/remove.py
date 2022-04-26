#luiz.augusto.farias@ccc.ufcg.edu.br

def remove_multiplos(fator, numeros):
    contador = 0
    for i in range(len(numeros)-1, -1, -1):
        if numeros[i] % fator == 0:
            numeros.pop(i)
            contador += 1

    return contador

numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(2, numeros) == 4
assert numeros == [5, 7, 3, 1]
numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(3, numeros) == 2
assert numeros == [2, 4, 5, 7, 10, 1]