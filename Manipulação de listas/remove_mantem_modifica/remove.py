# luiz.augusto.farias@ccc.ufcg.edu.br
# Remove Mantém ou Modifica

def remove_mantem_modifica(lista):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] % 3 == 0 and lista[i] % 4 == 0 and lista[i] % 5 == 0:
            lista[i] = 60
        elif lista[i] % 3 == 0 and lista[i] % 4 == 0:
            lista[i] = 12
        elif lista[i] % 4 == 0 and lista[i] % 5 == 0:
            lista[i] = 20
        elif lista[i] % 3 == 0 or lista[i] % 4 == 0 or lista[i] % 5 == 0:
            lista.pop(i)
    return None

l1 = [1, 2, 3, 120, 24]
l2 = [10, 20, 24, 31]
assert remove_mantem_modifica(l1) == None
assert remove_mantem_modifica(l2) == None
assert l1 == [1, 2, 60, 12]
assert l2 == [20, 12, 31] 

l3 = [1]
assert remove_mantem_modifica(l3) == None
l4 = [-1, -2, -3, -120, -24]
assert remove_mantem_modifica(l4) == None
l5 = [1, 2, 3, 3, 3, 120, 24, 3, 3, 3, 3]
assert remove_mantem_modifica(l5) == None