# luiz.augusto.farias@ccc.ufcg.edu.br  

def insere_ordenanda(lista, num):
    lista.append(num)
    
    for i in range(len(lista) - 1, -1, -1):
        if num > lista[i]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
    return lista

def noves_fora(lista):
    resultado = []
    copy_list = []
    for i in  range(len(lista)):
        copy_list.append(lista[i])

    resultado.append(copy_list)

    if len(copy_list) > 1:
        while True:
            mod = (lista[0] + lista[1]) % 9
            lista.pop(0)
            lista.pop(0)
            nova_lista = insere_ordenanda(lista, mod)

            copia = []
            for i in range(len(nova_lista)):
                copia.append(nova_lista[i])

            resultado.append(copia)
            if len(lista) == 1: break

        for elemento in resultado[-1]:
            resposta = elemento

    if len(copy_list) == 1:
        if lista == [9]:
            resultado = [[9], [0]]
            resposta = 0
        else:
            resultado = [[lista[0] % 9]]
            resposta = lista[0] % 9

    return (resposta ,resultado)


assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], 
                                              [7, 5, 4, 3, 1], 
                                              [4, 3, 3, 1], 
                                              [7, 3, 1], 
                                              [1, 1], 
                                              [2]])


assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])