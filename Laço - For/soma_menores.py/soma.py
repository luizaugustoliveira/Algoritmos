# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Soma Menores que Primeiro Elemento

menores = 0
soma = 0
lista = []
for e in range(11):
    num = int(input())
    lista.append(num)

for i in range(len(lista)):
    if lista[i] < lista[0]:
        menores += 1
        soma += lista[i]

print(f"menores = {menores}")
print(f"soma = {soma}")
