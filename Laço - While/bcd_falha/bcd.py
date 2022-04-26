def meu_in(elemento):
    sequencia = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001']
    for i in range(len(sequencia)):
        if sequencia[i] == elemento:          
            return True
    return False

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
    if meu_in(str(bcd1)) == True and  meu_in(str(bcd2)) == True:
        return num
    else:
        return f"BCD inválido."

while True:
    entrada = input()
    if entrada == "fim": break

    if len(entrada) > 8 or len(entrada) < 8:
        print("Tente novamente.")
    elif len(entrada) == 8:
        print(bcd(entrada))
