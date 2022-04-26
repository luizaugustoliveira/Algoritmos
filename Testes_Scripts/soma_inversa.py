def inverte(sequencia):
    if sequencia[0] == "-":
        numero_invertido = ""
    else:
        numero_invertido = "-"

    for i in range(len(sequencia) - 1, -1, -1):
        if sequencia[i] != "-":
            numero_invertido += sequencia[i]
    return numero_invertido

entrada = int(input())

for e in range(entrada):
    num = input().split()
    n1 = inverte(num[0])
    n2 = inverte(num[1])
    soma = int(n1) + int(n2) 
    soma_invertida = inverte(str(soma))
    print(soma_invertida)