def maioridade_penal(nomes, idades):
    lista_idades = idades.split()
    lista_nomes = nomes.split()
    acumulador = ""  
    for i in range(len(lista_idades)):
        if int(lista_idades[i]) >= 18:
            if i != len(lista_idades) - 1:
                acumulador += f"{lista_nomes[i]} "
            else:
                acumulador += f"{lista_nomes[i]}"

    return acumulador

# assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
# assert maioridade_penal("Jansen Italo Ana","14 15 16") == ""