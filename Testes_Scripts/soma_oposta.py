def inverte(lista):
    if lista[0] == "-":
        numero_invertido = ""
    else:
        numero_invertido = "-"

    for i in range(len(lista) - 1, -1, -1):
        if lista[i] != "-":
            numero_invertido += lista[i] 
    return numero_invertido

entrada = int(input())

for e in range(entrada):
    num = input().split()
    n1 = inverte(num[0])
    n2 = inverte(num[1])
    soma = int(n1) + int(n2)
    soma_invertida = inverte(str(soma))
    print(int(soma_invertida))








