import math

figura = input()

if figura == "círculo":
    raio = float(input())
    area_circulo = math.pi * (raio ** 2) 
    print(f"Área do círculo: {area_circulo:.2f} (cm2)")

elif figura == "retângulo":
    base_r = float(input())
    altura_r = float(input())
    area_retangulo = base_r * altura_r
    print(f"Área do retângulo: {area_retangulo:.2f} (cm2)")

elif figura == "quadrado":
    lado = float(input())
    area_quadrado = lado * lado
    print(f"Área do quadrado: {area_quadrado:.2f} (cm2)")
    
else:
    base_triangulo = float(input())
    altura_triangulo = float(input())
    area_triangulo = (base_triangulo * altura_triangulo) / 2
    print(f"Área do triângulo: {area_triangulo:.2f} (cm2)")