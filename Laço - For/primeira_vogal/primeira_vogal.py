# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Imprime Primeira Vogal

palavra = input()

vogais = ("aeiouAEIOU")

for letra in palavra:
    if letra in vogais:
        print(letra)
        break

if letra not in vogais:
    print("-")
    
