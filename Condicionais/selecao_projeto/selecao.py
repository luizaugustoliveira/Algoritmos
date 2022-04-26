# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Seleção Projeto

cre = float(input())
experiencia = int(input())
nota = int(input())

if cre >= 7:
    if experiencia >= 6:
        if nota > 3: 
            print("Candidato aprovado.")
        else:  # nota <= 3
            print("Candidato classificado.")
    else:      # experiencia < 6
        print("Candidato eliminado. Experiência abaixo do limite.")
else:          # cre < 7   
    if experiencia >= 6:
        print("Candidato eliminado. CRE abaixo do limite.")
    else:      # experiencia < 6
        print("Candidato eliminado. CRE e experiência abaixo do limite.")
