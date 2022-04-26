# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Posições de um elemento em uma sequência

def procura_valor(alvo, lista_percorrer):
    indices = []
    for i in range(len(lista_percorrer)):
        if lista_percorrer[i] == alvo:
            indices.append(i)
    
    return indices


def converte(lista):
    acumulador = ""
    primeiro = True
    for e in lista:
        if primeiro:
            acumulador += str(e)
            primeiro = False
        else:
            acumulador += " " + str(e)

    return acumulador

num = int(input())
sequencia = [int(seq) for seq in input().split()]

lista_indices = procura_valor(num, sequencia)

resposta = converte(lista_indices)

if lista_indices == []:
    print(-1)
else:
    print(resposta)
