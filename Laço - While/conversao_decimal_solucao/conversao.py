#luiz.augusto.farias@ccc.ufcg.edu.br

def inverte(sequencia):
    nova = ""
    for i in range(len(sequencia) - 1, -1 ,-1):
        nova +=sequencia[i]
    return nova

num = int(input())
quociente = num
hexadecimal = ""
while True:
    resto = quociente % 16
    if resto >= 10:
        hexadecimal += chr(97 + resto - 10)
    else:
        hexadecimal += str(resto)
    quociente = quociente // 16
    print(f"q = {quociente}, r = {resto}")
    if quociente == 0: break

print(inverte(hexadecimal))
    

