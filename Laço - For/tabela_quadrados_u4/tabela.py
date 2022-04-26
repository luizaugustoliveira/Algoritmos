# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Tabela de Quadrados

x = int(input())
y = int(input())

num = y - x

if x > y:
    print("---")
else:
    for i in range(num + 1):
        x_n = x + i
        x_quadrado = x_n ** 2
        print(f"{x_n} {x_quadrado}")
        
    
