fila = [219, 638, 263, 621, 482, 616]

def menor_que_seis(seq):
    # int(str(seq)[-1]) < 6
    return seq%10 < 6

def ajusta_prioridades(fila):
    prioridade, normal = [], []
    for i in range(len(fila)-1, -1, -1):
        if menor_que_seis(fila[i]):
            prioridade.append(fila.pop(i))
        else:
            normal.append(fila.pop(i))
    
    for i in range(len(prioridade)-1, -1, -1):
        fila.append(prioridade[i])
    
    for i in range(len(normal)-1, -1, -1):
        fila.append(normal[i])

print(fila)
ajusta_prioridades(fila)
print(fila)