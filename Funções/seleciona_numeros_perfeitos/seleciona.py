# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

def seleciona_perfeitos(lista):
    l1=[]
    l2=[6,28,496,8128,33550336]

    for i in range(len(lista)):
        if lista[i] in l2:
            l1.append(lista[i])
    
    return l1