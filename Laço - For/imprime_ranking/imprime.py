# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Imprime Ranking (Cumulativo)

n = int(input())

times, pontos = [], []
for i in range(n):
    times.append(input())
    pontos.append(input())

colocacoes = []
colocacao = 1
colocacao_acumulada = 0

for i in range(0, n):
    if i == 0:
        pass
    elif pontos[i] != pontos[i-1]:
        colocacao += colocacao_acumulada
        colocacao_acumulada = 0

    colocacoes.append(colocacao)
    colocacao_acumulada += 1

for i in range (n):
    print(f"{colocacoes[i]}. {times[i]} ({pontos[i]})")
    

