#luiz.augusto.farias@ccc.ufcg.edu.br

def perfeito(num):
    contador = 0
    soma = 0
    while True:
        contador += 1
        if contador == num: break
        if num % contador == 0:
            soma += contador
    
    if soma == num:
        return True
    else:
        return False


def seleciona_perfeitos(lista):
    perfeitos = []
    for i in range(len(lista)):
        if perfeito(lista[i]) == True:
            perfeitos.append(lista[i])
    return perfeitos

lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
assert seleciona_perfeitos(lista) == [6, 28]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]
