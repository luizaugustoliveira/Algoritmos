# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Sequência

limite = int(input())
soma = 0
expoente = 0
while True:
    soma += 2**expoente
    if soma >= limite:
        break
    print(2**expoente)
    expoente += 1
    

    