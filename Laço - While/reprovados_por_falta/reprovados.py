# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

def reprovados(sequencia):
    contador = 0
    indice = len(sequencia) -1
    while indice != 0:
        if sequencia[indice] == "f":
            contador += 1
        indice -= 1

    if contador > 8:
        return True
    else:
        return False
    
reprov = 0
while True:
    entrada = input()
    if entrada == "-": break

    if reprovados(entrada) == True:
        reprov += 1

print(f"{reprov} aluno(s) reprovado(s) por falta.")

