# luiz.augusto.farias@ccc.ufcg.edu.br

def soma(lista):
    total = 0
    for i in range(len(lista)):
        total += int(lista[i])
    return total


num = int(input())
contador = 0
n = 0
while n != num:
    entrada = input().split()
    n += 1
    if soma(entrada) == 0:
        contador += 1

print(contador)