# luiz.augusto.farias@ccc.ufcg.edu.br

contador = 0
soma = 0
while True:
    entrada = int(input())
    if entrada > 10:
        contador += 1

    if entrada <= 10:
        soma += entrada

    if soma >= 60: break
        
print(f"Rejeitadas = {contador}")        
print("Fim de semana!")


