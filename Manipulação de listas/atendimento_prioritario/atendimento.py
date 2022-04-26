def menor_que_seis(seq):
    lista = []
    string = str(seq)
    for i in range(len(string)):
        lista.append(string[i])
    
    if int(lista[-1]) < 6:
        return True
    else:
        return False
    

def ajusta_prioridades(fila):
    for indice in range(len(fila)):
        for i in range(indice, 0, -1):
            if menor_que_seis(fila[i]) and not menor_que_seis(fila[i-1]):
                fila[i], fila[i-1] = fila[i-1], fila[i]


fila = [327, 228, 516, 535, 248, 532]
assert ajusta_prioridades(fila) is None
assert fila == [535, 532, 327, 228, 516, 248]

fila = [219, 638, 263, 621, 482, 616]
assert ajusta_prioridades(fila) is None
assert fila == [263, 621, 482, 219, 638, 616]