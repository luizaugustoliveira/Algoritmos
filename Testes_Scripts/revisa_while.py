# Mais de uma sentinela

while True:
    soma = 0
    entrada = input()
    if entrada == "fim": break

    num = int(entrada)

    while True:
        if num == 0: break
        soma += num
        num = int(input())

    print(soma)