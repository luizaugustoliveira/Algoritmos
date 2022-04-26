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

def meu_lower(seq):
    acumulador = ""        
    acumulador += chr(ord(seq[0])+32)

    for i in range(1, len(seq)):
        acumulador += seq[i] 
    return acumulador

    
def gera_emails(nomes):
    emails = []
    for i in range(len(nomes)):
        nome = meu_split(nomes[i])
        emails.append(f"{meu_lower(nome[0])}.{meu_lower(nome[-1])}@ccc.ufcg.edu.br")
    return emails

nomes = ['Mariana Silva Lima', 'Joao Arthur', 'Pedro Alvares Cabral']
emails = ['mariana.lima@ccc.ufcg.edu.br', 'joao.arthur@ccc.ufcg.edu.br', 'pedro.cabral@ccc.ufcg.edu.br']
assert gera_emails(nomes) == emails