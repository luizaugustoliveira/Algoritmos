# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Primos até limite

def eh_primo(numero):
    lista = []
    for valor in range(1, numero +1):
        if numero % valor == 0:
            lista.append(valor)

    if lista == [1, numero]:
        return True
    else:
        return False

def primos_ate(limite):
    lista = []
    for num in range(2, limite):
        if eh_primo(num) == True:
            lista.append(num)

    return lista

