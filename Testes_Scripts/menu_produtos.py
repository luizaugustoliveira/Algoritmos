def meu_insert(lista, posicao, elemento):
    lista.append(elemento)
    for i in range(len(lista) - 1, -1, -1):
        if  i == posicao:
            break
        lista[i], lista[i - 1] = lista[i - 1], lista[i]

    return lista


def insere_produto(menu, produto, preco):
    tupla = (f"{produto}", preco)
    for i in range(len(menu) - 1, -1, -1):
        if preco < menu[i][1]:
            meu_insert(menu, i, tupla)
            break
        else:
            menu.append(tupla)
            break
    
    return menu


menu = [("expresso", 5.29), ("duplo", 8.09), ("capuccino", 10.59)]
insere_produto(menu, "latte", 9.59)
assert menu == [("expresso", 5.29), ("duplo", 8.09),
("latte", 9.59), ("capuccino", 10.59)]