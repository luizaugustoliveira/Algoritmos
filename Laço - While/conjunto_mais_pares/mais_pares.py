# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conjunto com mais pares

def conta_pares(lista):
    contador = 0 

    for elemento in lista:
        if elemento % 2 == 0:
            contador += 1

    return contador

def maior_elemento(lista):
    maior = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento 

    return maior


contagem = 0
ordem = 0
while True:
    lista = []
    nova_lista = []
    num = input()
    if num == "fim":
        break
    if num != "---":
        lista.append(int(num))
    elif num == "---":
        nova_lista.append(lista)
        ordem += 1

print(lista)
print(nova_lista)    
#print(f"Conjunto 4: 5 par(es)")