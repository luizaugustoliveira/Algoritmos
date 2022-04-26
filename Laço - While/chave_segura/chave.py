vogais = "AaEeIiOoUu"

conta_vogal = 0
conta_repetido = False
while True:
    entrada = input()
    
    for i in range(len(entrada)):
        if entrada[i] in vogais:
            conta_vogal += 1
    if conta_vogal > 5:
        print(f"Chave insegura. 6 vogais.")
        break

    
    for i in range(len(entrada) -1, -1, -1):
        if i != 0:
            if entrada[i] == entrada[i-1] == entrada[i-2]:
                conta_repetido = True
    if conta_repetido == True:
        print(f"Chave insegura. 3 caracteres consecutivos iguais.")
        break

    if conta_vogal > 5 and conta_repetido == True:
        print(f"Chave insegura. 6 vogais.")
        break


    

    




