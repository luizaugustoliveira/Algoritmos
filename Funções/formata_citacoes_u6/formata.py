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


def ultimo_nome(lista):
    nova_lista = meu_split(lista)
    return nova_lista[-1]


def fmt_citacao(lista):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(meu_split(lista[i]))

    ultimos = []
    for i in range(len(lista)):
        ultimos.append(ultimo_nome(lista[i]))

    primeiras = []
    for i in range(len(nova_lista)):
        primeiras.append(nova_lista[i][0])

    primeiras_letras = []
    for i in range(len(primeiras)):
        primeiras_letras.append(primeiras[i][0])
    
    citacao = []
    for i in range(len(ultimos)):
        citacao.append(f"{ultimos[i]}, {primeiras_letras[i]}.")

    return citacao

autores = [
    'Machado de Assis',
    'João Cabral de Melo Neto',
    'Graciliano Ramos',
    'Guimarães Rosa'
]

assert ultimo_nome(autores[0]) == 'Assis'
assert ultimo_nome(autores[1]) == 'Neto'
assert ultimo_nome(autores[2]) == 'Ramos'
assert ultimo_nome(autores[3]) == 'Rosa'

citacoes = fmt_citacao(autores)
assert citacoes == [
    'Assis, M.',
    'Neto, J.',
    'Ramos, G.',
    'Rosa, G.'
] 



