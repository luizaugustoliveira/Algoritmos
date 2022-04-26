# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

soma = 0
valores = []
while True:
    entrada = int(input())
    soma += entrada
    valores.append(entrada)
    if soma >= 999: break

media = soma / len(valores)
print(f"""{soma}
{media:.2f}""")

contador = 0
for i in range(len(valores)):
    if valores[i] > media:
        contador += 1
print(contador)
    
