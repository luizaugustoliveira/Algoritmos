num = int(input())

com = 0
sem = 0

for e in range(num):
    lista = []
    lista_sem = []
    palavras = input()
    for i in range(len(palavras)):
        if i != 0:
            if palavras[i] == palavras[i - 1]:
                lista.append(palavras)
            else:
                lista_sem.append(palavras)

    if lista != []:
        com += 1
    elif lista_sem != []:
        sem += 1

print(lista)
print(f"{com} palavra(s) com letras dobradas:")
for j in lista:
    print(i)

print("---")

print(f"{sem} palavra(s) sem letras dobradas:")
for e in lista_sem:
    print(e)
