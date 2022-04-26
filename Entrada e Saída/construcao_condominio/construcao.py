#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Construção de Condomínio

comprimento_terreno = float(input())
largura_terreno = float(input())
area_casa = float(input())

area_total = comprimento_terreno * largura_terreno

numero_casas = area_total // area_casa

n = int(numero_casas)

print(f"{n} casa(s) pode(m) ser construída(s) no terreno.")
