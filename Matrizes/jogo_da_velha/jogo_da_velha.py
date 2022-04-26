# luiz.augusto.farias@ccc.ufcg.edu.br

def metodo_auxiliar(lista):
    nova_lista = []
    existe = False
    resultado = 'Ninguem ganhou'
    for i in range(len(lista)):
        nova_lista.append(lista[i])
        if nova_lista == ['O','O','O']:
            existe = True
            mensagem = 'O ganhou'
    
    nova_lista1 = []
    for i in range(len(lista)):
        nova_lista1.append(lista[i])
        if nova_lista1 == ['X', 'X','X']:
            existe = True
            mensagem = 'X ganhou'

    if existe == True:
        return mensagem
    else:
        return resultado


def jogo_da_velha(tabuleiro):
    ordem = 3
    diagonal_1 = [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]]
    diagonal_2 = [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]
    resultado = metodo_auxiliar(diagonal_1)
    resultado = metodo_auxiliar(diagonal_2)

    for l in range(ordem):
        linha = []
        for coluna in range(ordem):
            linha.append(tabuleiro[l][coluna])
        resultado  = metodo_auxiliar(linha)
        if linha == ['O','O','O'] or linha == ['X', 'X','X']:break

    for c in range(ordem):
        coluna =[]
        for linha in range(ordem):
            coluna.append(tabuleiro[linha][c])
        resultado = metodo_auxiliar(coluna)
        if coluna == ['O','O','O'] or coluna == ['X', 'X','X']:break
            
    return resultado 
    
jogo1 = [['O', 'O', 'X'],
         ['X', 'O', 'O'],
         ['O', 'O', 'X']]
assert jogo_da_velha(jogo1) == 'O ganhou'



