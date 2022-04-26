def distribui_alunos(turma1, turma2, capacidade):
    indice = 0
    lcc1 = []
    lcc2 = []

    while True:
        if len(lcc1) < capacidade and (indice < len(turma1) or indice < len(turma2)):
            if len(lcc1) < capacidade and indice < len(turma1):
                lcc1.append(turma1[indice])
            if len(lcc1) < capacidade and indice < len(turma2):
                lcc1.append(turma2[indice])

        elif len(lcc2) < capacidade and (indice < len(turma1) or indice < len(turma2)):
            if len(lcc2) < capacidade and indice < len(turma1):
                lcc2.append(turma1[indice])
            if len(lcc2) < capacidade and indice < len(turma2):
                lcc2.append(turma2[indice])
        else:
            return [lcc1, lcc2]
        indice += 1
        

t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85, 17, 94]
assert distribui_alunos(t1, t2, 6) == [[10, 43, 38, 21, 87, 96], [22, 33, 25, 85, 17, 94]]

t1 = [10]
t2 = [43, 21, 96, 33, 85, 17, 94]
assert distribui_alunos(t1, t2, 6) == [[10, 43, 21, 96, 33, 85], [17, 94]]

t1 = [10]
t2 = [43, 21]
assert distribui_alunos(t1, t2, 6) == [[10, 43, 21], []]