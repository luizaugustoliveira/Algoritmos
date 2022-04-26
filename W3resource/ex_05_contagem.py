def contagem(lista):
    contador = 0

    for palavra in lista:
        if len(palavra) >= 2 and palavra[0] == palavra[-1]:
            contador += 1
    return contador


print(contagem(['abc', 'xyz', 'aba', '1221']))