#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Consumo de Energia

potencia = int(input())
minutos = int(input())

kw_potencia = potencia / 1000
tempo = minutos / 60

consumo = kw_potencia * tempo

print(f"{consumo:.1f} kWh")
