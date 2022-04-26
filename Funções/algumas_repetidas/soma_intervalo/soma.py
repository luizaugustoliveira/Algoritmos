def soma_intervalo(a, b):
    soma = 0
    for num in range(a , b + 1):
        soma += num
    return soma

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10