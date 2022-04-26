# luiz.augusto.farias@ccc.ufcg.edu.br 
# Questão: Obsfucation
# lembrar que strings são imutáveis
def obfusca(codigo):
    asteriscos = 0
    novo_codigo = ""
    for i in range(len(codigo)):
        if type(codigo[i]) == str:  
            if codigo[i].islower():
                novo_codigo += codigo[i].upper()
                asteriscos += 1
            elif codigo[i].isupper():
                novo_codigo += codigo[i].lower()
                asteriscos += 1
            elif codigo[i] == " ":
                novo_codigo += "*" * asteriscos
                asteriscos = 0
            else:
                novo_codigo += codigo[i]
                asteriscos += 1
        else:
            novo_codigo += codigo[i]
            asteriscos += 1

    codigo_final = ""
    for i in range(len(novo_codigo)):
        if novo_codigo[i] == "A" or novo_codigo[i] == "a":
            codigo_final += "4"
        elif novo_codigo[i] == "B" or novo_codigo[i] == "b":
            codigo_final += "8"
        elif novo_codigo[i] == "E" or novo_codigo[i] == "e":
            codigo_final += "3"
        elif novo_codigo[i] == "G" or novo_codigo[i] == "g":
            codigo_final += "6"
        elif novo_codigo[i] == "I" or novo_codigo[i] == "i":
            codigo_final += "1"
        elif novo_codigo[i] == "L" or novo_codigo[i] == "l":
            codigo_final += "7"
        elif novo_codigo[i] == "S" or novo_codigo[i] == "s":
            codigo_final += "5"
        elif novo_codigo[i] == "O" or novo_codigo[i] == "o":
            codigo_final += "0"
        elif novo_codigo[i] == "4":
            codigo_final += "A"
        elif novo_codigo[i] == "8":
            codigo_final += "B"
        elif novo_codigo[i] == "3":
            codigo_final += "E"
        elif novo_codigo[i] == "6":
            codigo_final += "G"
        elif novo_codigo[i] == "1":
            codigo_final += "I"
        elif novo_codigo[i] == "7":
            codigo_final += "L"
        elif novo_codigo[i] == "5":
            codigo_final += "S"
        elif novo_codigo[i] == "0":
            codigo_final += "O"
        else:
            codigo_final += novo_codigo[i]

    return codigo_final


while True:
    entrada = input()
    if entrada == 'fim': break
    print(obfusca(entrada))




        