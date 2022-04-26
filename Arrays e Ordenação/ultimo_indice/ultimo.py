def ultimo_indice(num, lista):
    existe = False
    for i in range(len(lista)):
        if lista[i] == num:
            existe = True
            posicao = i   
    
    if existe == True:
        return posicao
    else:
        return -1

assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
assert ultimo_indice(42, [15,2,13,11,14,2]) == -1