def conta_pares():
    contador = 0 
    while True:
        entrada = input()
        if entrada == "fim":
            return "fim"
        num = int(entrada)
        if entrada == "---":
            return contador
        if num % 2 == 0:
            contador += 1

def maior_elemento(lista):
    maior = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento 

    return maior

def indice_maior_elemento(lista):
    indice_maior = 0 
    for i in range(1, len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
    return indice_maior

def le_dados():
    conjuntos = []
    while True:
        
        

