def zera_nao_nulos(m, lin, col):
    linhas = len(m)
    colunas = len(m[0])

    for i in range(linhas):
        for j in range(colunas):
            if i == lin and i + 1 != 0:
                m[i][j] = 0

            if j == col and j + 1 != 0:
                m[i][j] = 0

    return m

jogo = [
[1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
]
zera_nao_nulos(jogo, 3, 2)
print(jogo)

