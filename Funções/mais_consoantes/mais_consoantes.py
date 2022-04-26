def contagem(seq):
    vogais = "AaEeIiOoUu"
    vogal = 0
    consoante = 0
    for i in range(len(seq)):
        if seq[i] in vogais:
            vogal += 1
        elif seq[i] not in vogais:
            consoante += 1

    if consoante > vogal:
        return True
    else:
        return False

contador = 0
while True:
    entrada = input()
    contagem(entrada)
    if contagem(entrada) == False:
        contador += 1
    elif contagem(entrada) == True: break

print(contador + 1)


