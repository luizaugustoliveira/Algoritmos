# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Dígitos Repetidos

def procura_digito(frase, letra):
    for i in range(len(frase)):
        if letra == frase[i +1] or letra == frase[i-1]:  
            return com += 1
        else:
            return sem += 1

num = int(input())

lista = []
for e in range(num):
    linhas = input()
    lista.append(linhas)

com = 0
sem = 0
for i in range(len(lista)):
    procura_digito(lista[i], lista)

#for i in range(len(lista)):
#    for e in range(len(lista[i])):
#        if lista[i][e] == lista[i][e + 1]:
#            com += 1
#        elif lista[i][e] == lista[i][e - 1]:
#            com += 1
#        else:
#            sem += 1

print(f"com: {com}")
print(f"sem: {sem}")

