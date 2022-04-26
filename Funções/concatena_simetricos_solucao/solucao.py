def ordem_alfabetica(seq1, seq2):
    if seq1[0] < seq2[0]:
        return f"{seq1}{seq2}"
    elif seq2[0] < seq1[0]:
        return f"{seq2}{seq1}"
    elif seq1[0] == seq2[0]:
        return f"{seq1}{seq2}"

def concatena_simetricos(lista):
    nova_lista = []
    if len(lista) % 2 == 0:
        for i in range(len(lista) // 2):
            acumulador = ""
            acumulador += ordem_alfabetica(lista[i], lista[len(lista) - 1 - i]) 
            nova_lista.append(acumulador)
    elif len(lista) % 2 == 1:
        for i in range(len(lista) // 2):
            acumulador = ""
            acumulador += ordem_alfabetica(lista[i], lista[len(lista) - 1 - i])
            nova_lista.append(acumulador)
        nova_lista.append(f"{lista[(len(lista) // 2)]}")
    
    return nova_lista

assert concatena_simetricos(["bola", "tv", "zebra", "arara"]) == ["ararabola", "tvzebra"]
assert concatena_simetricos(["ab", "cd", "ef", "gh", "ij"]) == ["abij", "cdgh", "ef"]
assert concatena_simetricos(["cd", "gh", "ck"]) == ["cdck", "gh"]