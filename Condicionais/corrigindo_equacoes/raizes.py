# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Corrigindo Equações

a = int(input())
b = int(input())
c = int(input())

delta = (b ** 2) - (4 * a * c)

x1 = ((-1*b) + (delta ** 0.5)) / (2 * a)
x2 = ((-1*b) - (delta ** 0.5)) / (2 * a)
x = (-1*b) / (2*a)

if delta > 0:
  print(f"x1 = {x1:.2f}")
  print(f"x2 = {x2:.2f}")
elif delta == 0:
  print(f"x = {x:.2f}")
else:
  print("sem raizes reais")
