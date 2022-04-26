# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != " ":
            acumulador += (sequencia[i])
        if sequencia[i] == " ":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    return lista

indice = 0
peso = 0
combustivel = 0
altitude = 0
while True:
    entrada = input()
    valores = meu_split(entrada)

    if int(valores[0]) >= 0:
        peso +=1
    else:
        indice = 0
        break

    if int(valores[1]) >= 0:
        combustivel += 1
    else:
        indice = 1
        break

    if int(valores[2]) >= 0:
        altitude += 1
    else:
        indice = 2
        break
        
if indice == 0:
    print(f"dado inconsistente. peso negativo.")
if indice == 1:
    print(f"dado inconsistente. combustível negativo.")
if indice == 2:
    print(f"dado inconsistente. altitude negativa.")

print(f"""peso: {peso}
combustível: {combustivel}
altitude: {altitude}""")
