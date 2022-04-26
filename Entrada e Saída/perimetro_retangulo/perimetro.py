#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Perímetro de retângulo

base = float(input())
altura = float(input())

base_cm = base / 10
altura_cm = altura / 10

perimetro = 2 * (base_cm + altura_cm)

print(f"O perímetro resultante (em cm) é {perimetro:.2f}.")
