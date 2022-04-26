#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
# Questão ingressos do cinema

adultos = int(input())
crianças = int(input())
preço_ingresso = float(input())

total = (adultos * preço_ingresso) + (crianças * preço_ingresso) / 2

print(f"Total: R$ {total:.2f}")
