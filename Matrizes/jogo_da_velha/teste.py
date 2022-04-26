            if i + j == ordem + 1:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if i == 0:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if i == 1:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if i == 2:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if j == 0:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if j == 1:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'

            if j == 2:
                if tabuleiro[i][j] == 'O':
                    resultado = 'O ganhou'
                else:
                    resultado = 'X ganhou'


 m = []
    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                m.append(tabuleiro[i][j])
    
    if m == ['O','O','O']:
        resultado = 'O ganhou'
    elif m == ['X', 'X','X']:
        resultado = 'X ganhou'
    else:
        resultado = 'Ninguem ganhou'

    s = []
    for i in range(ordem):
        for j in range(ordem):
            if i + j == ordem + 1:
                s.append(tabuleiro[i][j])

    if s == ['O','O','O']:
        resultado = 'O ganhou'
    elif s == ['X', 'X','X']:
        resultado = 'X ganhou'
    else:
        resultado = 'Ninguem ganhou'
