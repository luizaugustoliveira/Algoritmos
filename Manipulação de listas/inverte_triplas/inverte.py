# luiz.augusto.farias@ccc.ufcg.edu.br

def inverte3a3(string):
    lista = []
    s = ""
    contador = 0
    indice = 0

    for i in range(len(string)):
        s += string[i]
        contador += 1

        if contador % 3 == 0:
            lista.append(s)
            s = ''
            indice += 1

    acumulador = ""
    for i in range(len(lista) - 1, -1, -1):
        acumulador += lista[i]

    return acumulador

assert inverte3a3("abcdef") == "defabc"
assert inverte3a3("abcdefghijkl") == "jklghidefabc"
assert inverte3a3("111222333444") == "444333222111"