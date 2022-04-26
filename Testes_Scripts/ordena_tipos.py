def ordena_tipos(elementos):
    num = []
    letras = []
    outros_tipos = []
    for i in range(len(elementos)):
        if elementos[i].isdigit() == True:
            num.append(elementos[i]) 
        elif elementos[i].isalpha() == True:
            letras.append(elementos[i])
        else:
            outros_tipos.append(elementos[i])

    lista = num + letras + outros_tipos

    return lista

assert ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) \
== ['2', '4', '8', 'e', '1a', '4.4', 'e6']