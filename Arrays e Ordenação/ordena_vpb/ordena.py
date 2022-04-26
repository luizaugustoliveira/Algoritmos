# luiz.augusto.farias@ccc.ufcg.edu.br

def ordena_vpb(lista):

    for i in range(len(lista)):

        j = i

        while j > 0 and j <= i:

            if lista[j] > lista[j - 1]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1

