#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Quadrado na Circunferência

import math

raio_circunferencia = float(input())
lado_quadrado = raio_circunferencia * (2 ** 0.5)

area_circunferencia = math.pi * (raio_circunferencia ** 2)
area_quadrado = lado_quadrado ** 2 

area_diferenca = area_circunferencia - area_quadrado

print(f"Área não comum: {area_diferenca:.5f}")


