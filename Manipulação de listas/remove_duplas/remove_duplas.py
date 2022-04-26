# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 6 de outubro de 2021
# Questão: Remove Duplas

def remove_duplas(lista):
    for i in range(len(lista) -1, -1, -1):
        elemento = lista[i]
        contador = 0
        for numero in lista:
            if numero == elemento:
                contador += 1  

        if contador == 2:
            for indice in range(len(lista) -1, -1, -1):
                if lista[indice] == elemento:
                    lista.pop(indice) 

lista = [2,2,3,3,444]
assert remove_duplas(lista) == None
assert lista == [444]

lista = [5,7,8,9,55,55,33,22]
assert remove_duplas(lista) == None
assert lista == [5,7,8,9,33,22]