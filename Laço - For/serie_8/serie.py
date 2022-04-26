# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Série (8.8)

#8.8, 9.0, 9.2, 9.4, ..., 100.0
n = ((100 - 8.8) / 0.2) + 1

lista = []
for i in range(int(n)):
    lista.append(i)

for e in range(len(lista)):
    numeros = 8.8 + (lista[e] * 0.2)
    print(f"{numeros:.1f}")