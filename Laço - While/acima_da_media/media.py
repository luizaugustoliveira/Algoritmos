#luiz.augusto.farias@cc.ufcg.edu.br

def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += int(lista[i])
    m = soma / len(lista)
    return m


med = float(input())
acumulador = []
while True:
    entrada = input()
    if entrada == "fim": break
    valores = entrada.split()
    media(valores)
    if media(valores) < med / 2: break
    
    if media(valores) > med:
        acumulador.append(entrada)

for i in range(len(acumulador)):
    print(acumulador[i])