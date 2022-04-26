# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Validação de Triângulos

import math

lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

m1 = lado2 - lado3
m2 = lado1 - lado3
m3 = lado1 - lado2

perimetro = lado1 + lado2 + lado3
nperimetro = int(perimetro)

if math.fabs(m1) < lado1 < (lado2 + lado3) and math.fabs(m2) < lado2 < (lado1 + lado3) and math.fabs(m3) < lado3 < (lado1 + lado2):
    print(f"triangulo valido. {nperimetro}")
else:
    print(f"triangulo invalido.")
