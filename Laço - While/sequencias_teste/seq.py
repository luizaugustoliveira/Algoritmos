limite = int(input())

lista_numeros= []
for i in range(limite):
    lista_numeros.append(2 ** i)

soma = 0
while True:
    for i in range(len(lista_numeros)):
        soma += lista_numeros[i]
        if soma >= limite: break
        print(lista_numeros[i])
    if soma >= limite: break
