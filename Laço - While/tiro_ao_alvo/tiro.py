#UFCG
#luiz.augusto.farias@ccc.ufcg.edu.br

def dist(x, y):
    d = (((abs(x) - 0) ** 2) + ((abs(y) - 0) ** 2)) ** 0.5
    return d

contador = 0
lista = []
soma = 0
while True:    
    entrada = input().split()
    distancia = dist(float(entrada[0]), float(entrada[1]))
    lista.append(distancia)
    if distancia > 200: break 
    contador += 1
    soma += distancia
    print(f"{distancia:.2f}cm")

media = soma / (len(lista) - 1)

print(f"""--
num disparos: {contador}
distancia media: {media:.2f}cm""")



    
    