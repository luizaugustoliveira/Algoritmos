# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Soma os Múltiplos do Primeiro Elemento de uma Lista

lista = []
for n in range(11):
    num = int(input())
    lista.append(num)

soma = 0
for i in range(len(lista)-1, 0, -1):
    if lista[i] % lista[0] == 0:
        soma += lista[i]
print(soma)


