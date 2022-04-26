# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 9 de setembro de 2021
# Questão: Vizinhos Diferentes

quantidade_numeros = int(input())

lista = []
for i in range(quantidade_numeros):
    numero = int(input())
    lista.append(numero)

for i in range(len(lista) - 1, -1, -1):
    if lista[i] == lista[i - 1]:
        lista[i - 1] += 1

acumulador = ""
for i in range(len(lista)):
    if i != len(lista) - 1:
        acumulador += f"{str(lista[i])} "
    else:
        acumulador += f"{str(lista[i])}"

print(acumulador)