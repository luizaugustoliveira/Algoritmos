# luiz.augusto.farias@ccc.ufcg.edu.br
# Split

def split(frase, delimitador):
    lista = []
    acumulador = ""
    for i in range(len(frase)):
        if frase[i] != delimitador:
            acumulador += frase[i]
        else:
            lista.append(acumulador)
            acumulador = ""

    if acumulador != "":
        lista.append(acumulador)
    return lista

assert split('um exemplo', ' ') == ['um','exemplo']
assert split('testando', 'a') == ['test', 'ndo']
assert split("XXXX.XX.X.XXXXX", '.') == ['XXXX', 'XX', 'X', 'XXXXX']
