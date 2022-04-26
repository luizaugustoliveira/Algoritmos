valor = input()

lista = [int(valor[0]), int(valor[1])]
while True:
    soma = 0
    soma += lista[-1] + lista[-2]

    if soma <= int(valor):           
        lista.append(soma)

    if soma == int(valor):
        repdigit = True
        break

    if soma > int(valor):
        repdigit = False
        break

indice = 0
intervalo = len(lista)
while True:
    print(lista[indice])
    indice += 1

    if indice == len(lista): break

print("---")
if repdigit == True:
    print(f"{valor} é um repfigit.")
else:
    print(f"{valor} não é um repfigit.")   
