def long_words(n , palavras):
    long_terms = []
    lista = palavras.split()
    for i in range(len(lista)):
        if len(lista[i]) > n:
            long_terms.append(lista[i])

    return long_terms

print(long_words(3, "The quick brown fox jumps over the lazy dog"))