# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Binary Coded Decimal

def bcd(sequencia):
    algarismo1 = ""
    for i in range(0,4):
        algarismo1 += sequencia[i]
    bcd1 = int(algarismo1, 2)

    algarismo2 = ""
    for i in range(4,8):
        algarismo2 += sequencia[i]
    bcd2 = int(algarismo2, 2)

    num = str(bcd1) + str(bcd2)
    if bcd1 < 10 and bcd2 < 10:
        return num
    else:
        return f"BCD inválido."

while True:
    entrada = input()
    if entrada == "fim": break

    if len(entrada) != 8:
        print("Tente novamente.")
    elif len(entrada) == 8:
        print(bcd(entrada))

    


