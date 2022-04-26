
def tem_repetido(sequencia):
    for i in range(0, len(sequencia) - 1):
        if sequencia[i] == sequencia[i+1]:
            return True
    
    return False

num = int(input())
lista = []
for e in range(num):
    linhas = input()
    lista.append(linhas)
print(lista)

com = 0
sem = 0
for i in range(len(lista)):
    if tem_repetido(lista[i]):
        com += 1
    else:
        sem += 1

print(f"com: {com}")
print(f"sem: {sem}")