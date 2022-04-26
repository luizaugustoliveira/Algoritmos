# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Palavras com Letras Dobradas

# dei uma lida pra tentar amanhã

#an = a1 + (n-1)*r
n = (396 / 4) + 1

lista = []
for i in range(int(n)):
    lista.append(i)

for n in lista:
    num = 1 + (lista[n] * 4)
    print(num)
