#UFCG
#luiz.augusto.farias@ccc.ufcg.edu.br

numeros = []
soma = 0
while True:
    entrada = input()
    if entrada == "fim": break
    numeros.append(int(entrada))
    soma += int(entrada)

media = soma / len(numeros)
print(f"{media:.2f}")

for i in range(len(numeros)):
    if numeros[i] < media:
        print(f"{i + 1} {numeros[i]}")

