#luiz.augusto.farias@ccc.ufcg.edu.br

def meu_split(sequencia):
    lista = []
    acumulador = ""
    for i in range(len(sequencia)):
        if sequencia[i] != " ":
            acumulador += sequencia[i]
        if sequencia[i] == " ":
            if acumulador != "":
                lista.append(acumulador)
            acumulador = ""
    
    if acumulador != "":
        lista.append(acumulador)
    return lista

    
def gera_emails(lista):
    primeiros = []
    ultimos = []
    for i in range(len(lista)):
        nome = meu_split(lista[i])
        primeiros.append(nome[0].lower())
        ultimos.append(nome[-1].lower())

    emails = []
    for i in range(len(primeiros)):
        emails.append(f"{primeiros[i]}.{ultimos[i]}@ccc.ufcg.edu.br")
    return emails

nomes = ['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']
emails = ['mariana.lima@ccc.ufcg.edu.br', 'joao.arthur@ccc.ufcg.edu.br', 'pedro.cabral@ccc.ufcg.edu.br']
assert gera_emails(nomes) == emails