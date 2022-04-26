# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Tabela de Quadrados

x = int(input())
y = int(input())

for quadrados in range(x, y + 1):
    print(f"{quadrados} {quadrados ** 2}")
if x > y:
        print("---")
