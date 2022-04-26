# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Desenhando uma Árvore de Natal

altura = int(input())

espacos = altura 
n = 1
for e in range(altura):
    print(" " * (espacos - 1) + "o" * n)
    n = n + 2
    espacos = espacos - 1

#for e in range(altura):
#    o = ((2 * e) + 1) * "o"
#    print(" " * e + o)

print(" " * (altura - 1) + "o")
