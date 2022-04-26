# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Troca Coincidentes

palavra = input()
frase = list(palavra)
chave = input()

print(frase)


for i in range(len(frase)):
    if frase[i].isdigit():
        frase[i] = chave[int(frase[i])]

acumulador = ""
for letra in frase:
    acumulador += letra
    
print(acumulador)



        

