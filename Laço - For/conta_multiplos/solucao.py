# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conta múltiplos

num = int(input())
conjuntos = []

while True:
    entrada = input()
    if entrada == "fim": break
    conjuntos.append(entrada.split())

contador = 0    
for e in range(len(conjuntos)):
    if int(conjuntos[e][0]) % num == 0 and int(conjuntos[e][1]) % num == 0:
        contador += 1

print(contador)
