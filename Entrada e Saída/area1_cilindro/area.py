# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Área do Cilindro

import math

print("Cálculo da Superfície de um Cilindro")
print("---")
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2
area_base = math.pi * raio ** 2
area_lateral = 2 * math.pi * raio *  altura

area = 2 * area_base + area_lateral

print("---")
print(f"Área calculada: {area:.2f}")
