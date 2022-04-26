# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Grep

palavra = input()
num = int(input())

# a = palavra
# b == frase

for k in range(num):
    caracteres = 0
    frase = input()
    for i in range(len(frase)):
        if palavra[caracteres] == frase[i]:
            caracteres += 1
        else:
            caracteres = 0
    if caracteres == len(palavra):
        if True:
            break
        print(frase) 
    
#print(lista)

#letras == b
#palavra == a
#letras = ""
#caracteres = 0
#for l in range(len(lista)):
#    letras += lista[l]
#    for i in range(len(palavra)):
#        if palavra[caracteres] == letras[i]:
#            caracteres += 1
#        else:
#            caracteres = 0

#if caracteres == len(palavra):
#    print(letras)

#print(letras)
#    for n in range(len(letras) -2):
#        if letras[n] + letras[n+1] + letras[n+2] == palavra:
#            print(lista[i])

            
#print(string)







    