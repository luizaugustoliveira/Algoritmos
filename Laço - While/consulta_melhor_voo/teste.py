def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != "|":
            acumulador += sequencia[i]
        if sequencia[i] == "|": 
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    return lista

num = int(input())

while True:
    entrada = input()

    if entrada != "fim" and entrada != "valor" and entrada != "conexões" and entrada != "tempo":
        lista = meu_split(entrada)

        valor = lista[0]
        conexoes = lista[1]
        tempo = lista[2]
        companhia_atual = lista[3]

    if entrada == "valor":
        print(companhia_atual)

    if entrada == "fim": break

#print(valor)
#print(conexoes)
#print(tempo)
#print(companhia)




