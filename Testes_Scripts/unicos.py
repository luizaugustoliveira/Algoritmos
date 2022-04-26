def meu_in(sequencia, elemento):
    for valor in sequencia:
        if valor == elemento:          
            return True
    return False


def conta1(lista, elemento):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1

    if contador == 1:
        return True
    else:
        return False

def unicos_em_comum(seq1, seq2):
    menor = 0
    if len(seq1) < len(seq2):
        menor = seq1
    elif len(seq1) > len(seq2):
        menor = seq2
    else:
        menor = seq1

    lista = []
    for i in range(len(menor)):
        if conta1(seq1, menor[i]) == True and conta1(seq2, menor[i]):
            if meu_in(seq1, menor[i]) == True and meu_in(seq2, menor[i]) == True:
                lista.append(menor[i])

    return lista



