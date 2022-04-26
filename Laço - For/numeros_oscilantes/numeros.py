#luiz.augusto.farias@ccc.ufcg.edu.br

def saida(seq):
    retorno = False
    if len(seq) >= 2:
        for i in range(len(seq)):
            if i != len(seq) - 1:
                if int(seq[i]) % 2 == 0 and int(seq[i + 1]) % 2 == 1:
                    retorno = True
                
        for i in range(len(seq)):
            if i != len(seq) - 1:
                if int(seq[i]) % 2 == 1 and int(seq[i + 1]) % 2 == 0:
                    retorno = True

        for i in range(len(seq)):
            if i != len(seq) - 1:
                if int(seq[i]) % 2 == 0 and int(seq[i + 1]) % 2 == 0:
                    retorno = False

                if int(seq[i]) % 2 == 1 and int(seq[i + 1]) % 2 == 1:
                    retorno = False

    return retorno

entrada = input()

if saida(entrada) == True:
    print(f"verdadeiro: {len(entrada)} algarismos.")
elif saida(entrada) == False:
    print(f"falso: {len(entrada)} algarismos.")


