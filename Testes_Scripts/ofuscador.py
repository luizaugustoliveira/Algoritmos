def ofuscador(linha):
    asteriscos = 0
    nova_linha = ""
    for i in range(len(linha)):
        if type(linha[i]) == str:  
            if 97 <= ord(linha[i]) <= 122:
                nova_linha += chr(ord(linha[i]) - 32)
                asteriscos += 1
            elif 65 <= ord(linha[i]) <= 90:
                nova_linha += chr(ord(linha[i]) + 32)
                asteriscos += 1
            elif linha[i] == " ":
                nova_linha += "*" * asteriscos
                asteriscos = 0
            else:
                nova_linha += linha[i]
                asteriscos += 1
        else:
            nova_linha += linha[i]
            asteriscos += 1

    linha_final = ""
    for i in range(len(nova_linha)):
        if nova_linha[i] == "A" or nova_linha[i] == "a":
            linha_final += "4"
        elif nova_linha[i] == "B" or nova_linha[i] == "b":
            linha_final += "8"
        elif nova_linha[i] == "E" or nova_linha[i] == "e":
            linha_final += "3"
        elif nova_linha[i] == "G" or nova_linha[i] == "g":
            linha_final += "6"
        elif nova_linha[i] == "I" or nova_linha[i] == "i":
            linha_final += "1"
        elif nova_linha[i] == "L" or nova_linha[i] == "l":
            linha_final += "7"
        elif nova_linha[i] == "S" or nova_linha[i] == "s":
            linha_final += "5"
        elif nova_linha[i] == "O" or nova_linha[i] == "o":
            linha_final += "0"
        elif nova_linha[i] == "4":
            linha_final += "A"
        elif nova_linha[i] == "8":
            linha_final += "B"
        elif nova_linha[i] == "3":
            linha_final += "E"
        elif nova_linha[i] == "6":
            linha_final += "G"
        elif nova_linha[i] == "1":
            linha_final += "I"
        elif nova_linha[i] == "7":
            linha_final += "L"
        elif nova_linha[i] == "5":
            linha_final += "S"
        elif nova_linha[i] == "0":
            linha_final += "O"
        else:
            linha_final += nova_linha[i]

    return linha_final


linha = "I love Python!"
assert ofuscador(linha) == "1*70V3****pYTH0N!"
