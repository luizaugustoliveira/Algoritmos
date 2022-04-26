# luiz.augusto.farias@ccc.ufcg.edu.br  
# Alocação de aulas

def alocacao_aulas(alunos):
    nova_lista = [[], [], []]
    
    for i in range(len(alunos)):
        unidade = alunos[i][1]
        aluno = alunos[i][0]
        if  1 <= unidade <= 3:
            nova_lista[0].append(aluno)
        elif 4 <= unidade <= 6:
            nova_lista[1].append(aluno)
        else:
            nova_lista[2].append(aluno)

    return nova_lista


alunos = [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 10)]
assert alocacao_aulas(alunos) == [["Maria", "Carlos"],["João"],["Pedro", "Ângela"]]
assert alunos == [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 10)]

alunos = [("Maria", 3), ("João", 10)]
assert alocacao_aulas(alunos) == [["Maria"],[],["João"]]
assert alunos == [("Maria", 3), ("João", 10)]

