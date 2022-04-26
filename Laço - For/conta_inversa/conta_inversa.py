# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conta caracteres inversa

palavra = input()

palavra_inversa = []
for i in range(len(palavra) - 1, -1, -1):
    palavra_inversa += palavra[i]
    
contador = 0 
for l in range(len(palavra)):
    if palavra[l] == palavra_inversa[l]:
        contador += 1

print(f"A palavra {palavra} contém {contador} caractere(s) coincidente(s) com a sua inversa.")





