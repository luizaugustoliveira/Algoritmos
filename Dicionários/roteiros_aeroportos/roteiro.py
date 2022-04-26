def eh_roteiro(iata, voos, roteiro):
    cidades = roteiro.split("/")
    for i in range(len(cidades) - 1):
        validacao = False
        for sigla in voos[iata[cidades[i]]]: 
            if sigla == iata[cidades[i + 1]]:
                validacao = True
                break
        if not validacao: 
            return validacao

    return validacao