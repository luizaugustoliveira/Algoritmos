def soma_simetricos(valores):
    novos_valores = []
    if len(valores) % 2 == 0:
        for i in range(len(valores) // 2):
            soma = 0
            soma += valores[i] + valores[len(valores) - 1 - i] 
            novos_valores.append(soma)
    elif len(valores) % 2 == 1:
        for i in range(len(valores) // 2):
            soma = 0
            soma += valores[i] + valores[len(valores) - 1 - i]
            novos_valores.append(soma)
        novos_valores.append(valores[(len(valores) // 2)])
    
    return novos_valores

assert soma_simetricos([2, 5, 3, 9]) == [11, 8]
assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]