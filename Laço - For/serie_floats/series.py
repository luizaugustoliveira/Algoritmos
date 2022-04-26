# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Série: Sequencia de floats

razao = 1.5

lista = []
for i in range(15):
    lista.append(i)

for n in lista:
    num = 15.2 - (n * razao)
    print(f"{num:.1f}")
