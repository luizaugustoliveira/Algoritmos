num = int(input())

com = 0
sem = 0

for e in range(num):
    lista = []
    linhas = input()
    for i in range(len(linhas)):
        if i != 0:
            if linhas[i] == linhas[i-1]:
                lista.append(linhas[i])

    if lista != []:
        com += 1
    else:
        sem += 1

print(f"com: {com}")
print(f"sem: {sem}")