#luiz.augusto.farias@ccc.ufcg.edu.br

def maior_elemento(lista):
    maior = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento 

    return maior

def sequencia_caras(lista):
    contadores = []
    contador = 0
    while True:
        for i in range(len(lista) -1, -1, -1):
            if i != 0:
                if lista[i] == 1 and lista[i -1] == 1:
                    contador += 1
                elif lista[i] == 1 and lista[i -1] != 1:
                    break
        contadores.append(contador)
    
    resultado = maior_elemento(contadores)
    return resultado    


assert sequencia_caras([0,1,1,0,1,0,0,0]) == 2
assert sequencia_caras([1,0,1]) == 1
assert sequencia_caras([0,1,1,1,0]) == 3