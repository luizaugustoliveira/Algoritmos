# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Perímetro de um Triângulo

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

d12 = (((x1 - x2) ** 2) + ((y1 - y2 ) ** 2)) ** 0.5
d13 = (((x1 - x3) ** 2) + ((y1 - y3 ) ** 2)) ** 0.5 
d23 = (((x2 - x3) ** 2) + ((y2 - y3 ) ** 2)) ** 0.5 

perimetro = d12 + d13 + d23

print(f"O perímetro é de {perimetro:.2f}")
