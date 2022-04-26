#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: hipotenusa

import math

cateto1 = float(input("Medida do Cateto 1? "))
cateto2 = float(input("Medida do Cateto 2? "))
hipotenusa = math.hypot(cateto1, cateto2)

print(f"Medida da Hipotenusa: {hipotenusa:.2f}")


