# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 6 de outubro de 2021
# Questão: Analisa Equidistantes

def analisa_equidistantes(inteiros):
    if len(inteiros) % 2 == 0:
        nova_lista = []
        for i in range(len(inteiros) // 2):
            elemento1 = inteiros[i]
            elemento2 = inteiros[len(inteiros) - 1 - i]
            
            if elemento1 % 3 == 0 and elemento1 % 5 == 0 and elemento2 % 3 == 0 and elemento2 % 5 == 0:
                nova_lista.append(15)
            elif elemento1 % 3 == 0 and elemento2 % 3 == 0:
                nova_lista.append(3)
            elif elemento1 % 5 == 0 and elemento2 % 5 == 0:
                nova_lista.append(5)
            else:
                nova_lista.append(elemento1 * elemento2)

    elif len(inteiros) % 2 == 1:
        nova_lista = []
        for i in range(len(inteiros) // 2):
            elemento1 = inteiros[i]
            elemento2 = inteiros[len(inteiros) - 1 - i]
            
            if elemento1 % 3 == 0 and elemento1 % 5 == 0 and elemento2 % 3 == 0 and elemento2 % 5 == 0:
                nova_lista.append(15)
            elif elemento1 % 3 == 0 and elemento2 % 3 == 0:
                nova_lista.append(3)
            elif elemento1 % 5 == 0 and elemento2 % 5 == 0:
                nova_lista.append(5)
            else:
                nova_lista.append(elemento1 * elemento2)
        
        nova_lista.append(inteiros[(len(inteiros) // 2)])

    return nova_lista

assert analisa_equidistantes([3, 5, 15, 2, 80, 90, 45, 12]) == [3, 5, 15, 160] 
assert analisa_equidistantes([1, 27, 57, 18, 13]) == [13, 3, 57]
print(analisa_equidistantes([3, 5, 15,1,1,1,1,1,1]))