def imprime_lista(lista):
    for i in range(len(lista)):
        print("---")
        print(lista[i])

entrada = int(input())

lista = []
for i in range(entrada):
    nome = input()
    lista.append(nome)

imprime_lista(sorted(lista))
