#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Quadrado na Circunferência

import math

lado_quadrado = float(input())

diametro = lado_quadrado * (2 ** 0.5)
raio = diametro / 2

perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print(f"Perímetro: {perimetro:.5f}")
print(f"Área: {area:.5f}")
