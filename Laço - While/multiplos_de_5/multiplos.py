# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Múltiplos de 5

limite = int(input())
num = limite

lista = []
while True:
    if num % 5 == 0:
        if num % 2 == 0:
            lista.append(num)
    num -= 1
    if num == 0: break

for i in range(len(lista) - 1, -1, -1):
    if lista[i] < limite:
        print(lista[i])

