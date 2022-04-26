# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Votação na ADUF

abstencoes = int(input())
a_favor = int(input())
contra = int(input())
print("Resultado da Votação\n")

abstencoes_percent = (abstencoes * 100) / (abstencoes + a_favor + contra)
a_favor_percent = (a_favor * 100)/ (abstencoes + a_favor + contra) 
contra_percent = (contra * 100) / (abstencoes + a_favor + contra)

print(f"{abstencoes} abstenções ({abstencoes_percent:.2f}%)")
print(f"{a_favor} a favor ({a_favor_percent:.2f}%)")
print(f"{contra} contra ({contra_percent:.2f}%)")