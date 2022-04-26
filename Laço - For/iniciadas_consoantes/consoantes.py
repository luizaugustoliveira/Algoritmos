# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Iniciadas por consoantes

numero_palavras = int(input())

lista = []

for palavras in range(numero_palavras):
    palavra = input()
    lista.append(palavra)

print(f"total de palavras: {numero_palavras}")

vogais = ("aeiouAEIOU")

soma = 0
for valores in lista: 
    if valores[0] not in vogais:
        soma = soma + 1 

porcentagem = (soma / numero_palavras) * 100

print(f"iniciadas por consoantes: {soma} ({porcentagem:.2f}%)")
        



