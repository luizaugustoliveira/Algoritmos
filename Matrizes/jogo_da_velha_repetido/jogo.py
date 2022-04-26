def meu_in(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True

def jogo_da_velha(matriz):
    auxiliar = []
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(len(matriz)):
        auxiliar.append(matriz[i])
        for j in range(len(matriz)):
            if i == j:
                diagonal_principal.append(matriz[i][j])
            if i + j == len(matriz) - 1:
                diagonal_secundaria.append(matriz[i][j])

    auxiliar.append(diagonal_principal)
    auxiliar.append(diagonal_secundaria)

    for i in range(len(matriz)):
        coluna = []
        for j in range(len(matriz)):
            coluna.append(matriz[j][i])

        auxiliar.append(coluna)
    
    if meu_in(['X', 'X','X'], auxiliar) == True:
        resultado = 'X ganhou'
    elif meu_in(['O','O','O'], auxiliar):
        resultado = 'O ganhou'
    else:
        resultado = 'Ninguem ganhou'

    return resultado

