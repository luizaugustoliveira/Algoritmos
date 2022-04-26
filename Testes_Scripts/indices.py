# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Índices de caracteres

#Plano

#    1. Ler a frase a ser inspecionada
#    2. Ler a string que define as letras a inspecionar

#    3. Pra cada letra da string:
#    3.1 Procurar onde ela aparece na frase
#       Acumular as posições numa lista
#    3.2 Imprimir as posicoes onde ela ocorre

def procura_frase(frase, letra):
    lista = []
    for i in range(len(frase)):
        if letra == frase[i]:
            lista.append(i)
    return lista

def converte(lista):
    acumulador = ""
    primeiro = True
    for e in lista:
        if primeiro:
            acumulador += str(e)
            primeiro = False
        else:
            acumulador += " " + str(e)
    return acumulador

frase = input()
a_inspecionar = input()

for letra in a_inspecionar:
    lista = procura_frase(frase, letra)
    resposta = converte(lista)
    if lista == []:
        print(-1)
    else:
        print(resposta)

