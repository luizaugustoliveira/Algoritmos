# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Frase com Maior Palavra

def maior_elemento(lista):
    maior = lista[0]

    for elemento in lista:
        if len(elemento) > len(maior):
            maior = elemento 

    return maior


lista_maiores = []
while True:
    entrada = input()
    if entrada == "fim": break

    palavras = entrada.split()

    maior_palavra = maior_elemento(palavras)
    lista_maiores.append(maior_palavra)

palavra = lista_maiores[0]
for i in range(len(lista_maiores)):
    if len(lista_maiores[i]) > len(palavra):
        palavra = lista_maiores[i]

for indice in range(len(lista_maiores)):
    if lista_maiores[indice] == palavra:
        posicao = indice + 1

print(f"Frase {posicao}: {palavra}")

    

