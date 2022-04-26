# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conta múltiplos

def busca(lista, valor):
    contador = 0
    for i in range(len(lista)):
        if int(lista[i]) % valor == 0:
            contador += 1
            return contador

num = int(input())


for e in range(num+1):
    seq = input().split()

sequencia = []
for j in range(len(seq)):
    sequencia.append(seq[j])

for i in range(len(sequencia)):
    resposta = busca(sequencia, num)

print("fim")
print(resposta)

def conta_multiplos(lista, num):
    for elemento in range(len(lista)):
        if elemento[0] % num == 0 and elemento[1] % num == 0:
            return True
    return False

num = int(input())

lista = []
for i in range(num + 1):
    numeros = input().split()
    lista.append(numeros)

cont = 0
for elemento in lista:
    if conta_multiplos(elemento, num) == True:
        cont += 1

print("fim")
print(cont)