# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Forma Palavra a partir de Outras 3 Palavras

lista = []
for e in range(3):
    palavra = input().split
    lista.append(palavra)

nova_palavra = ""
for e in range(len(lista)):
    for i in range(len(lista[i])):
        if lista[e][i] > lista[e+1][i] > lista[e+2][i]:
            nova_palavra += lista[e][i]
        elif lista[e+1][i] > lista[e][i] > lista[e+2][i]:
            nova_palavra += lista[e+1][i]
        else:
            nova_palavra += lista[e+2][i]
            
print(nova_palavra)

