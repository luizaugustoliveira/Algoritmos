#luiz.augusto.farias@ccc.ufcg.edu.br

num1 = input()
num2 = input()

lista1 = []
for i in range(len(num1)):
    lista1.append(int(num1[i]))

lista2 = []
for i in range(len(num2)):
    lista2.append(int(num2[i]))

soma = 0
numeros = []
posicao = []
for i in range((len(lista1))):
    if lista1[i] == lista2[i]:
        if lista1[i] % 2 == 0:
            numeros.append(lista1[i])
            posicao.append(i + 1)

print("Dígitos coincidentes")
for i in range(len(numeros)):
    print(f"{numeros[i]} na posição {posicao[i]}")

soma = 0
for elemento in numeros:
    soma += elemento
print(f"Soma de dígitos coincidentes: {soma}")
