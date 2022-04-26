# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Criptografando uma Senha

palavra = input()

nova_palavra = ""
contador = 0
for indice in range(len(palavra)):
    letra = palavra[indice]
    if indice == 0:
        nova_palavra += letra
    else:
        if letra in "AaEeIiOo":
            if letra == "A" or letra == "a":
                nova_palavra += "4"
                contador += 1
            elif letra == "E" or letra == "e":
                nova_palavra += "3"
                contador += 1
            elif letra == "I" or letra == "i":
                nova_palavra += "1"
                contador += 1
            elif letra == "O" or letra == "o":
                nova_palavra += "0"
                contador += 1
        else:
            nova_palavra += letra

print(f"{nova_palavra} ({contador} troca(s))")

        



