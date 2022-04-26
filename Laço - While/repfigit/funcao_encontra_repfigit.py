def encontra_repfigit(num):
    valor = str(num)
    penultimo_termo = int(valor[0])
    ultimo_termo = int(valor[1])
    soma = ultimo_termo + penultimo_termo

    while True:
        ultimo = ultimo_termo
        ultimo_termo = soma
        soma = soma + ultimo
        
        if soma == int(valor):
            return True
        
        if soma > int(valor):
            return False

numeros = []
for numero in range(10, 100):
    if encontra_repfigit(numero) == True:
        numeros.append(numero)

print(numeros)
numeros = [14, 19, 28, 47, 61, 75]
