# luiz.augusto.farias@ccc.ufcg.edu.br  

def move_direita(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == '*' and labirinto[i][j + 1] == ' ':
                labirinto[i][j], labirinto[i][j + 1] = labirinto[i][j + 1], labirinto[i][j]
                return (i , j + 1)
            
            if labirinto[i][j] == '*' and labirinto[i][j + 1] != ' ':
                resultado = (i, j)
                break
            
    return resultado

labirinto1 = [
  ['P', '*', ' ', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]

assert move_direita(labirinto1) == (0, 2)

assert labirinto1 ==  [
  ['P', ' ', '*', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]

labirinto2 = [
  ['P', 'P', ' ', ' '],
  ['P', '*', 'P', ' '],
  ['P', 'P', 'P', ' '],
]
assert move_direita(labirinto2) == (1, 1)