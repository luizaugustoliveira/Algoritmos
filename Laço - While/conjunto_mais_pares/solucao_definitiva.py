def conta_pares():
    contador = 0 
    while True:
        entrada = input()
        if entrada == "fim": return "fim"
        if entrada == "---": return contador
        if int(entrada) % 2 == 0: contador += 1

def indice_maior_elemento(lista):
    indice_maior = 0 
    for i in range(1, len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
    return indice_maior

conjuntos = []
while True:
    pares = conta_pares()
    if pares == "fim": break
    conjuntos.append(pares)
    imaior = indice_maior_elemento(conjuntos)
#    print(pares)
#print(conjuntos)
print(f"Conjunto {imaior + 1}: {conjuntos[imaior]} par(es)")



        

