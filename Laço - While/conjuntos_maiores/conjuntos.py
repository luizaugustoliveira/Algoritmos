# luiz.augusto.farias@ccc.ufcg.edu.br

def soma(lista):
    soma = 0
    for elemento in lista:
        soma += elemento    

    return soma

limite = int(input())
quantidade = int(input())

conjuntos = []
contador = 0
conjunto = []
while True:
    if contador == quantidade: break
    
    valor = int(input())
    if valor == -1:
        conjuntos.append(conjunto)
        contador += 1
        conjunto = []
    else:
        conjunto.append(valor)


if conjuntos != []:
    for i in range(len(conjuntos)):
        if soma(conjuntos[i]) > limite:
            print(f"conjunto {i + 1}: {soma(conjuntos[i])}")
