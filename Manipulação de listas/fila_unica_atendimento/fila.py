# luiz.augusto.farias@ccc.ufcg.edu.br

def gera_filas(fila, n):
    lista = []
    for i in range(n):
        lista.append([])

    contador = 0
    for i in range(len(fila)):
        lista[contador].append(fila[i])
        contador += 1
        if contador % n == 0:
            contador = 0

    return lista

fila_1 = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
assert gera_filas(fila_1, 3) == [['Andre','Carlos'],['Antonio', 'Claudia'], ['Bianca']]

fila_2 = ['Andre', 'Antonio', 'Bianca', 'Carlos']
assert gera_filas(fila_2, 2) == [['Andre','Bianca'],['Antonio', 'Carlos']]