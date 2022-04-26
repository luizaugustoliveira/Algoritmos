# luiz.augusto.farias@ccc.ufcg.edu.br

def intersecao_listas(l1,l2):
    for i in range(len(l1)-1,-1,-1):
        InLista = False
        for num in l2:
            if num == l1[i]:
                InLista = True
        if not InLista:
            l1.pop(i)
    
    return l1