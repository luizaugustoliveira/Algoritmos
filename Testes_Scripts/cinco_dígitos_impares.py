def tem(lista,elemento):
    for valor in lista:
        if valor == elemento:
            return True
    return False

lista = input().split() 

contador = 0
for i in range(len(lista)):
        if tem(lista[i], '1') and tem(lista[i], '3') and tem(lista[i],'5') and tem(lista[i], '7') and tem(lista[i],'9'):
            contador +=1

print(contador)

