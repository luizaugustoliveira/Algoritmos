# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Troca Coincidentes

posicoes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

palavra = input()
frase = list(palavra)
chave = input()

for i in range(len(frase)):
    if frase[i].isdigit():
        frase[i] = chave[int(frase[i])]

acumulador = ""
for letra in frase:
    acumulador += letra
    
print(acumulador)



        

