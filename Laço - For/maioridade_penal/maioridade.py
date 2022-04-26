# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 9 de setembro de 2021
# Questão: Maioridade Penal

pessoas = input().split()
idades = input().split()  

for i in range(len(idades)):
    if int(idades[i]) >= 18:
        print(pessoas[i])