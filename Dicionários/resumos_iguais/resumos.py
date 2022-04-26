# luiz.augusto.farias@ccc.ufcg.edu.br

def soma_algarismos(numero):
    num = str(numero)
    soma = 0
    for i in range(len(num)):
        soma += int(num[i])
    return soma

def agrupa_resumos_iguais(lista):
    agrupamento = {}

    for e in lista:
        mensagem = ""
        if soma_algarismos(e) in agrupamento.keys():
            mensagem = "entrou no if"
            agrupamento[soma_algarismos(e)].append(e)
        else:
            mensagem = "entrou no else"
            agrupamento[soma_algarismos(e)] = [e]

    return agrupamento


lista1 = [60, 343, 19, 1230, 51, 123]
assert agrupa_resumos_iguais(lista1) == {6:[60, 1230, 51, 123], 10:[343,19]}