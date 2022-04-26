# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Imprime Ranking (Cumulativo)

n = int(input())

lista_times = []
lista_pontos = []

for k in range(n):
    times = input()
    pontos = int(input())
    lista_times.append(times)
    lista_pontos.append(pontos)

contador = 0
colocacao = 0
for e in range(len(lista_pontos)):
    if lista_pontos[e] == lista_pontos[e] + 1:
        contador += 1
        colocacao += contador
    elif lista_pontos[e] != lista_pontos[e] + 1:
        colocacao += contador

for i in range(n):
    print(f"{i+contador}. {lista_times[i]} ({lista_pontos[i]})")





