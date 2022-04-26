#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Conversão para Graus Decimais

graus = int(input())
minutos = int(input())
segundos = int(input())

minutos_para_graus = minutos / 60

segundos_para_graus = segundos / 3600

ngraus = graus + minutos_para_graus + segundos_para_graus

print(f"graus = {ngraus:.4f}")
