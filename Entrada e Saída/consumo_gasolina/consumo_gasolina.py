#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Consumo de gasolina

posicao_inicial = float(input())
quantidade_litros_posicao_inicial = float(input())
posicao_final = float(input())
quantidade_litros_posicao_final = float(input())

distancia = posicao_final - posicao_inicial
litros = quantidade_litros_posicao_inicial - quantidade_litros_posicao_final

consumo = distancia / litros

print(f"{consumo:.1f}")

