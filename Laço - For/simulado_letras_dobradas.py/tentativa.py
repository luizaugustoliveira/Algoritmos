def letra_repetida(sequencia):
    for i in range(0, len(sequencia) - 1):
        if sequencia[i] == sequencia[i + 1]:
            return True
    return False

num = int(input())

palavras = []
for i in range(num):
    palavras.append(input())

lista_repetidas = []
repetidas = 0
lista_sem_repetir = []
sem_repetir = 0
for i in range(len(palavras)):
    if letra_repetida(palavras[i]) == True:
        repetidas += 1
        lista_repetidas.append(palavras[i]) 
    else:
        sem_repetir += 1
        lista_sem_repetir.append(palavras[i])

print(f"{repetidas} palavra(s) com letras dobradas:")
for j in lista_repetidas:
    print(j)

print("---")

print(f"{sem_repetir} palavra(s) sem letras dobradas:")
for k in lista_sem_repetir:
    print(k)
