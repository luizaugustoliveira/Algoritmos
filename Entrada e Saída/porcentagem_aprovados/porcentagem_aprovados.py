# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Percentagem de aprovados

print("Análise da Turma")
print("===")
aprovados = int(input("Número de aprovados? "))
reprovados = int(input("Número de reprovados? "))

total = aprovados + reprovados
percent_aprovados = (aprovados / total) * 100
percent_reprovados = (reprovados / total) * 100

print("---")
print(f"Total de alunos na turma: {total}")
print(f"Aprovados: {aprovados} = {percent_aprovados:.1f}%")
print(f"Reprovados: {reprovados} = {percent_reprovados:.1f}%")
