# luiz.augusto.farias@ccc.ufcg.edu.br

def cesar(msg, d):
    acumulador = ""
    for i in range(len(msg)):
        if 97 <= ord(msg[i]) <= 122:
            if ord(msg[i]) + d > 122:
                acumulador += chr(96 + (ord(msg[i]) + d - 122))
            elif ord(msg[i]) + d < 97:
                acumulador += chr(ord(msg[i]) + d + 26)
            else:
                acumulador += chr(ord(msg[i]) + d)
        else:
            acumulador += msg[i]

    return acumulador
    

assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
#print(cesar("zzz aaa yyy eee", 100))
#print(cesar("zzz aaa yyy eee", -4))
#print(cesar("zzz aaa yyy eee Z A P ZUM 9283549!@#$%¨&&**)(", 4))             



             