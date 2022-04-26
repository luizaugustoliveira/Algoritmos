# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Classificação de Elementos Utilizando a Média dos Extremos

lista = []
num_n = int(input())
for linhas in range(num_n):
    l = int(input())
    lista.append(l)

menor = lista[0]
for elemento in lista:
    if elemento < menor:
        menor = elemento
print(f"Menor número: {menor}")

maior = lista[0]
for elemento in lista:
    if elemento > maior:
        maior = elemento 
print(f"Maior número: {maior}")

media = (maior + menor) / 2
print(f"Média dos extremos: {media:.2f}")

contador_menor = 0
contador_maior = 0
for num in lista:
    if num < media:
        contador_menor += 1
    elif num > media:
        contador_maior +=1
print(f"{contador_menor} número(s) abaixo da média")
print(f"{contador_maior} número(s) acima da média")
