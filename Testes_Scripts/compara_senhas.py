def compara_senhas(senha1, senha2):
    tamanho1 = len(senha1)
    tamanho2 = len(senha2)

    menor = 0
    if tamanho1 < tamanho2:
        menor = tamanho1
    elif tamanho2 < tamanho1:
        menor = tamanho2
    else:
        menor = tamanho1

    contador = 0
    for i in range(menor):
        if senha1[i] != senha2[i]:
            contador += 1
    
    return contador

assert compara_senhas('nome123', 'nome') == 0
assert compara_senhas('aaa', 'bbb') == 3
assert compara_senhas('senha', 'Senha') == 1