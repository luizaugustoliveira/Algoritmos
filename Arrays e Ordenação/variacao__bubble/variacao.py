def variacao_bubble(vetor, ini, fim):
    contador = 0
    fim -= 1
    while (ini < fim):
        if vetor[ini] > vetor[fim]:
            vetor[ini], vetor[fim] = vetor[fim], vetor[ini]
            contador += 1
        ini += 1
        fim -= 1

    return contador

vetor = [8, 6, 9, 2, 3, 1, 4, 0, 7, 4]
assert variacao_bubble(vetor, 1, 7) == 2
assert vetor == [8, 4, 1, 2, 3, 9, 6, 0, 7, 4]