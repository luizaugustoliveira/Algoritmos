# luiz.augusto.farias@ccc.ufcg.edu.br

def time_campeao(dados):
    pontos = []
    for lista in dados.values():
        pontos.append(lista[0])

    maior = pontos[0]
    for i in range(len(pontos)):
        if pontos[i] > maior:
            maior = pontos[i]

    campeao = []
    for time, valores in dados.items():
        if valores[0] == maior:
            campeao.append(time)

    return campeao

dados = {"Botafogo": [59, 43, 39],
    "São Paulo": [52, 44, 36],
    "Palmeiras": [80, 62, 32],
    "Santos": [72, 59, 35]}

assert time_campeao(dados) == ["Palmeiras"]