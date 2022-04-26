# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Troca Coincidentes

palavra = input()
chave = input()

frase = ""
for i in range(10):
    if palavra[i] == str(i):
        frase += chave[i]
    else:
        frase += palavra[i]

for e in range(10 ,len(palavra)):
    frase += palavra[e]

print(frase)


        

