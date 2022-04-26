# luiz.augusto.farias@ccc.ufcg.edu.br

def quase_fonemas(palavra):
    lista = []
    vogais = "AaEeIiOoUu"
    for i in range(len(palavra) - 1):
        if palavra[i] not in vogais and palavra[i + 1] in vogais:
            lista.append(f"{palavra[i]}{palavra[i + 1]}")

    return lista
