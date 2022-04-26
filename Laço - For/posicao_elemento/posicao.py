# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Posições de um elemento em uma sequência

num = int(input())
sequencia = input()

lista = sequencia.split(" ") 

def meu_in(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
        else:
            return -1

print(meu_in(lista, num))
