# luiz.augusto.farias@ccc.ufcg.edu.br   


def pega_diagional(matriz):
  diagonal = []
  count = 0
  for i in range(len(matriz) - 1, -1, -1):
    diagonal.append(matriz[i][count])
    count += 1

  return diagonal

def rotaciona_ds(matriz, direcao):
  diagonal_secundaria = pega_diagional(matriz)

  if direcao == "cima":
    ultimo_el = diagonal_secundaria.pop()
    diagonal_secundaria = [ultimo_el] + diagonal_secundaria
  else:
    primeiro_el = diagonal_secundaria.pop(0)
    diagonal_secundaria.append(primeiro_el)
  
  count = len(diagonal_secundaria) - 1
  for i in range(len(diagonal_secundaria)):
    matriz[i][count] = diagonal_secundaria[count]
    count -= 1
  
  return matriz

M = [[1, 2, 3, 4 ], [5, 6, 7, 8 ], [9, 10, 11, 12], [14, 15, 16, 17]]
print(rotaciona_ds(M, 'cima'))
print(rotaciona_ds(M, 'baixo'))
