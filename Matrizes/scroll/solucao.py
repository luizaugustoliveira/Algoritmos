# luiz.augusto.farias@ccc.ufcg.edu.br

def scroll(lista):
    for i in range(len(lista)):
        if i != 0:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
        elif i == 0:
            for j in range(len(lista[0])):
                lista[0][j] = 0

m = [[  1,  2,  3,  4 ],
     [  5,  6,  7,  8 ],
     [  9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ],
     [ 17, 18, 19, 20 ]]

scroll(m)
assert m == [[  5,  6,  7,  8 ],
             [  9, 10, 11, 12 ],
             [ 13, 14, 15, 16 ],
             [ 17, 18, 19, 20 ],
             [  0,  0,  0,  0 ]]
