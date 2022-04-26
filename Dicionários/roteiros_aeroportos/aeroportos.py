# luiz.augusto.farias@ccc.ufcg.edu.br

def meu_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True

def eh_roteiro(iata, voos, cidades):
    lista = cidades.split("/")
    
    for i in range(len(lista) - 1):
        if meu_in(voos[iata[lista[i]]], iata[lista[i + 1]]) == False:
            return False
    return True

iata = {"Campina Grande": "CPV",
       "Recife": "REC",
       "Salvador": "SSA",
       "Brasilia": "BSB",
       "Sao Paulo": "GRU",
       "Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],
       "REC": ["CPV", "BSB", "GRU", "GIG"],
       "SSA": ["REC", "GRU", "GIG"],
       "BSB": ["CPV", "GIG", "GRU"],
       "GRU": ["GIG", "BSB"],
       "GIG": ["GRU", "REC"]}

assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")