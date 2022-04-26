def conta_pares(lista):
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
    return pares

pares = []
conjuntos = []
while True:
    entrada = input()
    if entrada == "fim": break
    if entrada != "---":
        conjuntos.append(int(entrada))

    while True:
        entrada = input()
        if entrada == "---":
            pares.append(conta_pares(conjuntos))
            conjuntos = []
            break
        else:
            conjuntos.append(int(entrada))

maior = pares[0]
for i in range(len(pares)):
    if pares[i] > maior:
        maior = pares[i]
        posicao = i + 1

print(f"Conjunto {posicao}: {maior} par(es)")

