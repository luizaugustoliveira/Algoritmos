# luiz.augusto.farias@ccc.ufcg.edu.br

def is_substring(str1, str2):
    indice = 0
    acumulador = ""
    operacoes = 0
    while True:
        if len(acumulador) == len(str2):
            operacoes += 1
            indice = operacoes
            if acumulador == str2:
                return True

            acumulador = ""

        if indice == len(str1): break

        acumulador += str1[indice]
        indice += 1
    

assert is_substring('boiada','iada')
assert is_substring('boiada','boi')
assert is_substring('boiada','ada')
assert not is_substring('casorio', 'casa')
assert is_substring('boiada','b')
assert is_substring('boiada','bo')
assert is_substring('boiada','boiad')