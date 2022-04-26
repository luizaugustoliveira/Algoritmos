#UFCG
#luiz.augusto.farias@ccc.ufcg.edu.br

def maior_indice(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[maior]:
            maior = i

    return maior


def maior_turma(turmas, alunos_turma):
    if alunos_turma == []: return ""

    maior = maior_indice(alunos_turma)

    return f"{turmas[maior]}: {alunos_turma[maior]} aluno(s)\n"


turmas = []
alunos_turma = []
while True:
    turma = input()
    if turma == "fim": break

    turmas.append(turma)
    alunos = 0
    while True:
        matricula = input()
        if matricula == "-1": break
        alunos += 1
    
    alunos_turma.append(alunos)

print(maior_turma(turmas, alunos_turma), end = "")