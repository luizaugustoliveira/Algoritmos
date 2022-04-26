par_por_conjunto = []
while True:
    entrada = input()
    if entrada == "fim": break

    conta_par = 0
    while True:
        if entrada == "---": break
        
        num = int(entrada)
        if num % 2 == 0:
            conta_par += 1

        entrada = input()
    par_por_conjunto.append(conta_par)


maior = par_por_conjunto[0]
for i in range(len(par_por_conjunto)):
    if par_por_conjunto[i] > maior:
        maior = par_por_conjunto[i]
        posicao = i + 1

print(f"Conjunto {posicao}: {maior} par(es)")

    


    


