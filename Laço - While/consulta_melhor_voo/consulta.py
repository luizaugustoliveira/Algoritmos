# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Consulta Melhor Voo

def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != "|":
            acumulador += sequencia[i]
        if sequencia[i] == "|":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    return lista

def menor_elemento(lista):
    menor = float(lista[0])
    indice = 0
    for i in range(len(lista)):
        lista[i] = float(lista[i])
        if lista[i] < menor:
            menor = lista[i]
            indice = i

    return indice

num = int(input())

lista_valores = []
lista_tempo = []
lista_conexoes = []
lista_companhias = []
contador = 0
while contador != num:
    entrada = meu_split(input())
    contador += 1

    lista_valores.append(entrada[0])
    lista_tempo.append(entrada[1])
    lista_conexoes.append(entrada[2])
    lista_companhias.append(entrada[3])

while True:
    entrada = input()

    if entrada == "fim": break 

    if entrada == "valor":
        print(lista_companhias[menor_elemento(lista_valores)])

    if entrada == "tempo":
        print(lista_companhias[menor_elemento(lista_tempo)])

    if entrada == "conexoes":
        print(lista_companhias[menor_elemento(lista_conexoes)])

#print(lista_valores)
#print(lista_tempo)
#print(lista_conexoes)
#print(lista_companhias)
#print(menor_elemento(lista_valores))







