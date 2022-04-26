# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Forma Palavra a partir de Outras 3 Palavras

def meu_max(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

palavras = []
for e in range(3):
    palavras.append(input())

acumulador = ""
for i in range(len(palavras[0])):
    acumulador += meu_max(palavras[0][i], palavras[1][i], palavras[2][i])

print(acumulador)


