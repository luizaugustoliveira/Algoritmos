def conta_pares():
    contador = 0 
    while True:
        entrada = input()
        if entrada == "fim": return "fim"
        if entrada == "---": return contador
        if int(entrada) % 2 == 0: contador += 1
        

def indice_maior_elemento(lista):
    indice_maior = 0 
    for i in range(len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
    return indice_maior


pares_em_conjuntos = []
while True:
    pares = conta_pares()
    if pares == "fim": break
    if pares > 0:
        pares_em_conjuntos.append(pares)


imaior = indice_maior_elemento(pares_em_conjuntos)
if pares_em_conjuntos != []:
    print(f"Conjunto {imaior + 1}: {pares_em_conjuntos[imaior]} par(es)")




        

