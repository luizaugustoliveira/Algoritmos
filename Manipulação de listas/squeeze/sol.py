def squeeze(valores):
    indice =0
    while True:
        if valores[indice] == valores[indice +1]:
            valores.pop(indice)
            indice -=1
        indice +=1
    
        if indice == len(valores) -1: break

    return valores

nums = [7, 3, 3, 5, 8, 8, 8, 4, 3]
assert squeeze(nums) == [7, 3, 5, 8, 4, 3]