pares = 0
maior_par = 0
conjunto = 0
maior_conjunto = 0

while True:
    entrada = input()

    if entrada == "---":
        conjunto += 1
        if pares > maior_par:
            maior_par = pares
            maior_conjunto = conjunto 
            pares = 0
        else:
            pares = 0

    elif entrada == "fim": break

    elif int(entrada) % 2 == 0:
        pares += 1

if maior_conjunto > 0 and maior_par > 0:
    print(f'Conjunto {maior_conjunto}: {maior_par} par(es)')
