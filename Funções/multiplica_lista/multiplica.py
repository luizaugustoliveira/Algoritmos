def multiplica_lista(n,lista):
    nova_lista = []
    contador = 0
    if n != 0:
        while True:
            nova_lista += lista
            contador += 1
            if contador == abs(n): break

    return nova_lista

