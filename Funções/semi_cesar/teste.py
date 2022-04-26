def cesar(texto, delta):
    nova_string = ''
    for e in texto:
        if e.isalpha() == True:
            if ord(e) > 90:
                if chr(ord(e) + delta) > 'z':
                    nova_string += chr((ord(e) + delta) - 26)
                else:
                    nova_string += chr(ord(e) + delta)
            else:
                if chr(ord(e) + delta) > 'Z':
                    nova_string += chr((ord(e) + delta) - 26)
                else:
                    nova_string += chr(ord(e) + delta)
        else:
            nova_string += e
    return nova_string

assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"