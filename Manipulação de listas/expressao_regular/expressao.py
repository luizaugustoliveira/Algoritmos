# luiz.augusto.farias@ccc.ufcg.edu.br

def is_substring_expr(str1,str2):
    lista = []
    acumulador = ""
    for i in range(len(str2)):
        if str2[i] != "*":
            acumulador += str2[i]
        if str2[i] == "*":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    
    palavra1 = lista[0]
    palavra2 = lista[1]
    acumulador1 = ""
    for i in range(len(palavra1)):
        acumulador1 += str1[i]

    acumulador2 = ""
    indice = -(len(palavra2))
    while True:
        acumulador2 += str1[indice]
        indice += 1
        if indice == 0: break

    if palavra1 == acumulador1 and palavra2 == acumulador2:
        return True
    else:
        return False

assert is_substring_expr('oicarovoce','oi*voce')
assert is_substring_expr('oicvoce','oi*voce')

