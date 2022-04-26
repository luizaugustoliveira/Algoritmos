while True:
    soma = 0
    entrada = input()
    if entrada == "fim": break

    while True:
        if entrada == "---": break
        num = int(entrada)
        soma += num
        entrada = input()

    print(soma)
