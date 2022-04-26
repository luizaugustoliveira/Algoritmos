def busca(seq, valor):
    existe = False
    for i in range(len(seq)):
        if seq[i] == valor:
            existe = True
            posicao = i
            break

    if existe == True:
        return posicao
    else:
        return -1    

seq = [8, 9, 2, 3, 6, 10, 7, 9]
assert busca(seq, 6) == 4
assert busca(seq, 4) == -1
assert busca(seq, 9) == 1
assert busca(seq, 8) == 0