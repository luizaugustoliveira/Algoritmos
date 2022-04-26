vogais = "AaEeIiOoUu"

entrada = input()

i = 0
v = 0
consecutivos = 0
caractere_anterior = entrada[0]
while i != len(entrada):
    caractere = entrada[i]

    if caractere in vogais:
        v += 1

    if v > 5:
        print(f"Chave insegura. 6 vogais.")
        break

    if caractere == caractere_anterior:
        consecutivos += 1
    else:
        caractere_anterior = caractere
        consecutivos = 1

    if consecutivos >= 3:
        print("Chave insegura. 3 caracteres consecutivos iguais.")
        break

    i += 1

if v < 5 and consecutivos < 3:
    print(f"Chave segura!")




