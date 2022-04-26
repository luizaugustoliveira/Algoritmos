# luiz.augusto.farias@ccc.ufcg.edu.br

def remove_repetidos(lista):
    for i in range(len(lista) -1, -1, -1):
        for j in range(len(lista) -1, -1, -1):
            if i != j:
                if lista[j] == lista[i]:
                    lista.pop(i)
                    break

digitos = [1, 1, 2, 2, 5, 1]
assert remove_repetidos(digitos) == None
assert digitos == [1, 2, 5]
digitos = [1, 2, 1, 2, 1, 1]
assert remove_repetidos(digitos) == None
assert digitos == [1, 2]