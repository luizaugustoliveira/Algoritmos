# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Palavras com Letras Dobradas

# dei uma lida pra tentar amanhã

palavra = input()

letras = ""
for i in range(len(palavra)):
    if i % 2 == 0:
        letras += palavra[i]
print(letras)