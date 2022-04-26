# luiz.augutsto.farias@ccc.ufcg.edu.br

def meu_in(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False


def filtra_alunos(aluno_media, matriculas, media):
    contador = 0 
    for i in range(len(aluno_media) - 1, -1, -1):
        if meu_in(matriculas, aluno_media[i][0]) == False:
            aluno_media.pop(i)
            contador += 1  

    for i in range(len(aluno_media) - 1, -1, -1): 
        if aluno_media[i][1] < media:
            aluno_media.pop(i)
            contador += 1  

    return contador


inscritos = [121, 123, 124]
alunos =  [ (120,8.0), 
            (121,7.5), 
            (122,5.0), 
            (123,6.0), 
            (124,9.0), 
            (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]