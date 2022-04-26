def altera_vetor_por_escalar(lista, fator):
    resultado=[]
    for i in range(len(lista)):
        resultado.append(lista.pop())
    for j in range(len(resultado)-1,-1,-1):
        lista.append(int(resultado[j])*int(fator))
    return None

vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]