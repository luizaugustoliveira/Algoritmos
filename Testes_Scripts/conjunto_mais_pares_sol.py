def conta_pares(lista):
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
    return pares

conjunto = []
pares = 0

while True:
    entrada = input()
    if entrada == "fim": break

    if entrada == "---":
        if conta_pares(conjunto) > pares:
            pares = conta_pares(conjunto)

        conjunto = []
    else:
        conjunto.append(int(entrada))
        





    
    


