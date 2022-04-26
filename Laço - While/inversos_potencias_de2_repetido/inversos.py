# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Inversos das Potências de 2 - Série Convergente

import math

p = float(input())

alvo = 2/3
soma = 0

i = 0
while True:
    if abs(alvo - soma) > p:
        print(f"{soma:.14f}")
    else:
        print(f"{soma:.14f}")
        break

    soma += ((-1)**i) * (1 / 2**i)

    i += 1

    
    
