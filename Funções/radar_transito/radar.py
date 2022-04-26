#luiz.augusto.farias@ccc.ufcg.edu.br

def radar_transito(velocidade_maxima, tempo):
    distancia = 2
    v = distancia / tempo
    velocidade = v * 3.6

    if velocidade <= velocidade_maxima:
        return ["Ok", 0.0]

    elif velocidade_maxima < velocidade <= 1.1 * velocidade_maxima:
        return ["Leve", 87.5]

    elif velocidade_maxima < velocidade <= 1.5 * velocidade_maxima:
        return ["Média", 127.5] 

    elif velocidade_maxima < velocidade > 1.5 * velocidade_maxima:
        return ["Grave", 577.5]
        
print(radar_transito(80.0, 0.1))
print(radar_transito(80.0, 0.085))
print(radar_transito(80.0, 0.07))
print(radar_transito(80.0, 0.05))

assert radar_transito(80.0, 0.1) == ["Ok", 0.0]
assert radar_transito(80.0, 0.085) == ["Leve", 87.5]
assert radar_transito(80.0, 0.07) == ["Média", 127.5]
assert radar_transito(80.0, 0.05) == ["Grave", 577.5]