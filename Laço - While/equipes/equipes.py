# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 6 de outubro de 2021
# Questão: Equipes

contador = 0
while True:
    entrada = input()
    if entrada == "-": break
    contador += 1  

if contador == 11:
    print("Modalidade -> Futebol")
elif contador == 5:
    print("Modalidade -> Basquete")
elif contador == 6:
    print("Modalidade -> Vôlei")
elif contador == 7:
    print("Modalidade -> Handebol")
else:
    print("Equipe Inválida")