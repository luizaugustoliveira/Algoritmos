# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conta ímpares

num = int(input())

lista = []
for e in range(num):
    numeros = int(input())
    lista.append(numeros)

contador = 0
for elemento in lista:
    if elemento % 2 == 1:
        contador += 1

percent = (contador / num) * 100

print(f"{contador} ({percent:.1f}%)")
