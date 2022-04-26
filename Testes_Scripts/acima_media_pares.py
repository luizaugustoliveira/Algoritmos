entrada = int(input())

soma = 0
contador = 0
lista = []
for i in range(entrada):
    numero = int(input())
    lista.append(numero)
    if numero % 2 == 0:
        soma += numero
        contador += 1

media = soma / contador

conta = 0
for i in range(len(lista)):
    if lista[i] > media:
        conta += 1

print(f"média dos pares: {media:.1f}")
print(f"acima da média: {conta}")