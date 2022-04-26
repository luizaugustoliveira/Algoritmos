# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Caixa Preta

num_n = int(input())

lista = []
for i in range(num_n):
    linhas = input()
    lista.append(linhas)

lista_linhas = []
for m in lista:
    medicoes = m.split(' ')
    lista_linhas.append(medicoes)

valores = []
for j in range(len(lista_linhas)):
    valores += lista_linhas[j]

contador = 0
for k in range(len(valores)):
    if int(valores[k]) < 0:
        if (k + 3) % 3 == 0:
            print("dado inconsistente. peso negativo.")
        elif (k + 2) % 3 == 0:
            print("dado inconsistente. combustível negativo.")
        elif (k + 1) % 3 == 0:
            print("dado inconsistente. altitude negativa.")
        break
    elif int(valores[k]) >= 0:
        contador += 1
print(f"{contador} dados válidos.")


