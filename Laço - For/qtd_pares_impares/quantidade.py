# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Quantidade de Números Pares e Ímpares

num = int(input())

inteiros = []
for e in range(num):
    inteiros.append(int(input()))

pares = 0
lista_pares = []
soma_par = 0
impares = 0
lista_impares = []
soma_impar = 0
for i in range(len(inteiros)):
    if inteiros[i] % 2 == 0:
        pares += 1
        lista_pares.append(inteiros[i])
        soma_par += inteiros[i]
    else:
        impares += 1
        lista_impares.append(inteiros[i])
        soma_impar += inteiros[i]

media_pares = soma_par / pares
media_impares = soma_impar / impares

print(f"""pares: {pares}
ímpares: {impares}
média pares: {media_pares:.1f}
média ímpares: {media_impares:.1f}""")
   



