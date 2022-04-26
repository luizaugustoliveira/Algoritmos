# luiz.augusto.farias@ccc.ufcg.edu.br
# Filtra Pares

limite = int(input())

lista = []
contador = 0
while True:
    entrada1 = input()
    if entrada1 == "": break

    entrada2 = input()
    acumulador = ""

    if int(entrada1) + int(entrada2) > limite:
        contador += 1
        acumulador += f"{int(entrada1)} {int(entrada2)}"
        lista.append(acumulador)

    if int(entrada2) == 0: break
    print(f">> {contador} até o momento")
    

#print(lista)
if lista != []:
    for i in range(len(lista)) :
        print(lista[i])
