# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Busca na Frase

frase = input()

chave = input()
lista_chave = list(chave)
#print(lista_chave)

lista_iguais = []
for i in range(len(frase)):
    for j in range(len(lista_chave)):
        if frase[i] == lista_chave[j]:
            lista_iguais.append(frase[i])
#print(lista_iguais)

if len(lista_chave) < len(lista_iguais):
    limite = len(lista_chave)
else:
    limite = len(lista_iguais)

contador = 0
for i in range(limite):
    if lista_chave[i] == lista_iguais[i]:
        contador += 1
    print(f"{lista_chave[i]} {contador}")
