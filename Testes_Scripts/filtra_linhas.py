invalidas = 0
contador = 0
while True:
    entrada = input()
    
    if entrada == "fim":
        print(f"sequências lidas: {contador} (inválidas: {invalidas})")
        break

    contador += 1
    sequencia = entrada.split()
    pares = 0
    impares = 0
    for i in range(len(sequencia)):
        if int(sequencia[i]) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    if impares > pares:
        invalidas += 1
        print(f"linha {contador} inválida: {entrada}")
