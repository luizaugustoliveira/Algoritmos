#luiz.augusto.farias@ccc.ufcg.edu.br

def sequencia_caras(lista):
    maior_elemento_sequencia = 0
    contador = 0
    for i in range(len(lista)):
        if lista[i] == 1:
            contador += 1
        elif lista[i] == 0:
            if contador >= maior_elemento_sequencia:
                maior_elemento_sequencia = contador
            contador = 0
    
    if contador >= maior_elemento_sequencia:
        maior_elemento_sequencia = contador
            
    return maior_elemento_sequencia

assert sequencia_caras([0,1,0,0,0,0,1,1]) == 2
assert sequencia_caras([0,1,1,0,1,0,0,0]) == 2
assert sequencia_caras([1,0,1]) == 1
assert sequencia_caras([0,1,1,1,0]) == 3
assert sequencia_caras([0,0,0,0]) == 0
