# luiz.augusto.farias@ccc.ufcg.edu.br
# Ordena 3 Números

n1 = int(input())
n2 = int(input())
n3 = int(input())

maior = 0
segundo_maior = 0
terceiro_maior = 0

if n1 > n2:
    maior = n1
    segundo_maior = n2
else:
    maior = n2
    segundo_maior = n1

if n3 > maior:
    terceiro_maior = segundo_maior
    segundo_maior = maior
    maior = n3
elif n3 > segundo_maior:
    terceiro_maior = segundo_maior
    segundo_maior = n3
else:
    terceiro_maior = n3

print(f"{terceiro_maior} {segundo_maior} {maior}")