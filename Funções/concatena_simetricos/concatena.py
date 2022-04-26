# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

def primeira_letra(seq1,seq2):
    for i in range(seq1):
        if seq1[i] > seq2[i]:
            return seq1 + seq2
        elif seq2[i] > seq1[i]:
            return seq2 + seq1

def concatena_simetricos(lista):
    pares = []
    impares = []
    for i in range(len(lista)):
        if i % 2 == 0:
            pares.append(lista[i])
        else:
            impares.append(lista[i])

    if len(pares) == len(impares):
        for i in range(len(pares)):
            primeira_letra(pares[i],impares[i])

print(concatena_simetricos(["bola", "tv", "zebra", "arara"]))
