# luiz.augusto.farias@ccc.ufcg.edu.br


def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != ".":
            acumulador += sequencia[i]
        if sequencia[i] == ".":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""

    if acumulador != "":
        lista.append(acumulador)

    return lista


def indexa(nome_completo, indice):
	lista_de_nomes = meu_split(nome_completo)
    validacao = False
    lista = []
	for i in nome_completo:
        if (i.lower() in indice): 
            lista = indice[i]
            if (not nome_completo in lista):
                lista.append(nome_completo)
                validacao = True
        else:
            indice[i] = [nome_completo]]

    return validacao
	 

#print(indexa("Jose Silva", indice))