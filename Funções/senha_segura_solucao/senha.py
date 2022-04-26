#luiz.augusto.farias@ccc.ufcg.edu.br

def senha_segura(seq):
    acumulador = ""
    if len(seq) >= 4:
        for i in range(len(seq)):
            if (i+1) % 2 == 0:
                if int(seq[i]) % 2 == 0:
                    acumulador += "v"
            elif (i+1) % 2 == 1:
                if int(seq[i]) % 2 == 1:
                    acumulador += "v"

    if acumulador == "v" * len(seq):
        return "Senha segura"
    else:
        return "Senha insegura"

print(senha_segura("1"))
