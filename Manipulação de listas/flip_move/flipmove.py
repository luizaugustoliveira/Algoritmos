# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Flipmove

def flipmove(lista, k):
  iteracao = k//2
  for i in range(iteracao):
    lista[i], lista[(k-1)-i] = lista[(k-1)-i], lista[i]
  for i in range(k):
    lista.append(lista.pop(0))

lista = [5, 8, 3, 7, 1, 6, 4, 9, 2]
flipmove(lista, 4)
assert lista == [1, 6, 4, 9, 2, 7, 3, 8, 5]
lista2 = [5, 8, 3, 7, 1, 6, 4, 9, 2]
flipmove(lista2, 2)
assert lista2 == [3, 7, 1, 6, 4, 9, 2, 8, 5]

    