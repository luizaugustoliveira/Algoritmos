# luiz.augusto.farias@ccc.ufcg.edu.br
# Caracteres

def meu_in(palavra, elemento):
    for i in range(len(palavra)):
        if palavra[i] == elemento:
            return True
    return False

def palavras_com_caractere(palavras, caractere):
    contador = 0
    for i in range(len(palavras)):
        if meu_in(palavras[i], caractere) == True:
            contador += 1

    return contador


assert palavras_com_caractere(["casa", "carro", "teste"], "x") == 0
assert palavras_com_caractere(["casa", "carro", "teste"], "r") == 1
assert palavras_com_caractere(["casa", "carro", "teste"], "a") == 2