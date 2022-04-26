# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Teste de Lâmpadas

def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != ".":
            acumulador += sequencia[i]
        if sequencia[i] == ".":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    return lista


while True:
    entrada = input()
    if entrada == ".X.X.X.X.X": break
    seq_falhas = meu_split(entrada)
    if seq_falhas == []:
        print("0 falhas")
    else:
        contador = 0
        acumulador = ""
        for i in range(len(seq_falhas)):
            contador += len(seq_falhas[i])
            if i == len(seq_falhas) - 1:
                acumulador += str(len(seq_falhas[i]))
            else:
                acumulador += f"{str(len(seq_falhas[i]))} + "
        print(f"{contador} falha(s): {acumulador}")
        
        





