def meu_split(string, separador):
    palavra = ''
    saida = []
    for s in range(len(string)):
        if string[s] != separador : palavra += string[s]
        else:
            saida.append(palavra)
            palavra = ''
    saida.append(palavra)

    return saida

def indexa(nome_completo, indice):
	alterou = False
	list_nome = meu_split(nome_completo, ' ')
	for nome in list_nome:
		if nome.lower() in indice and nome_completo not in indice[nome.lower()]: 
			indice[nome.lower()].append(nome_completo)
			alterou = True
		elif nome.lower() not in indice: 
			indice[nome.lower()] = [nome_completo]
			alterou = True
	
	return alterou