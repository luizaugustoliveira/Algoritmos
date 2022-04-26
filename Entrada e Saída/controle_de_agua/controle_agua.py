# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Controle de Água

import math

velocidade = float(input())
diametro = float(input())
tempo = float(input())

secao = math.pi * (diametro / 2) ** 2
vazao = velocidade * secao * 1000
quant_agua = tempo * vazao

print(f"Quantidade de água = {quant_agua:.2f} litros.")
