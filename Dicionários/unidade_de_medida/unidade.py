# luiz.augusto.farias@ccc.ufcg.edu.br

medidas = {'km': 1000, 'hm':100, 'dam':10, 'm':1, 'dm':0.1, 'cm':0.01, 'mm':0.001}

resultados = []

while True:
    soma = 0
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[2])

    if x == 0 and y == 0: break

    for i in range(0, len(entrada), 2):
        valor = int(entrada[i]) * medidas[entrada[i +1]]
        soma += valor
    resultados.append(soma)

for i in range(len(resultados)):
    print(f'{resultados[i]:.2f} m')