# luiz.augusto.farias@ccc.ufcg.edu.br

def is_substring(str1, str2):
    acumulador = ""
    contador = 0
    indice = 0
    while True:
        if indice == len(str1): break
        acumulador += str1[indice]
        indice += 1
        contador += 1
        
        if contador == len(str2):
            if acumulador == str2:
                return True
            else:
                contador = 0
                acumulador = ""
                indice = len(str1) - len(str2)
    return False

assert is_substring('boiada','iada')
assert is_substring('boiada','boi')
assert is_substring('boiada','ada')
assert not is_substring('casorio', 'casa')