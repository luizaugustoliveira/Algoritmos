# luiz.augusto.farias@ccc.ufcg.edu.br

def meu_in(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def tem_afinidade(l1, l2):
    if len(l1) > len(l2):
        maior = l1
        menor = l2
    else:
        maior = l2
        menor = l1

    contador = 0
    for i in range(len(menor)):
        if meu_in(maior, menor[i]) == True:
            contador += 1

    if contador >= 3:
        return True
    else:
        return False


